#!/usr/bin/env python3

import yt_dlp
import sys
import os
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QFileDialog
from datetime import datetime
import dbus
import time

# Función para enviar notificaciones usando dbus en KDE
def send_notification(summary, body, notification_id=None, actions=None):
    bus = dbus.SessionBus()
    notify = bus.get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications")
    notify_interface = dbus.Interface(notify, "org.freedesktop.Notifications")
    
    if notification_id is None:
        notification_id = 0
        
    app_name = "YouTube Downloader"
    icon = "dialog-information"
    timeout = 5000  # Milisegundos, 5000 = 5 segundos
    hints = {}
    
    # Acciones opcionales
    if actions is None:
        actions = []
    
    notification_id = notify_interface.Notify(
        app_name,              # App Name
        notification_id,        # Replace ID (0 for new)
        icon,                  # Icon
        summary,               # Title
        body,                  # Body Text
        actions,               # Action Buttons
        hints,                 # Hints (empty)
        timeout                # Timeout
    )
    
    return notification_id

# Función para descargar el audio en formato .mp3 con progreso
def download_audio(url, save_path):
    notification_id = send_notification("Descarga iniciada", "Iniciando descarga de audio...")

    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d['_percent_str'].strip()
            speed = d['_speed_str'].strip()
            eta = d['_eta_str'].strip()
            message = f"Progreso: {percent}\nVelocidad: {speed}\nTiempo restante: {eta}"
            send_notification("Descargando audio...", message, notification_id=notification_id)
        elif d['status'] == 'finished':
            send_notification("Descarga completada", "Conversión a mp3 completada.", notification_id=notification_id)

    # Opciones para la descarga
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook]  # Hook de progreso
    }

    # Descargar el archivo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url)
        downloaded_file = os.path.join(save_path, f"{info_dict['title']}.mp3")
    
    # Cambiar la fecha de modificación del archivo al día de hoy
    if os.path.exists(downloaded_file):
        now = datetime.now().timestamp()  # Obtener la marca de tiempo actual
        os.utime(downloaded_file, (now, now))  # Cambiar la fecha de acceso y modificación

    # Notificación final con un botón de cerrar
    send_notification("Descarga completada", "El archivo de audio ha sido guardado correctamente.", notification_id=notification_id, actions=["default", "Cerrar"])

# Función para obtener la URL del portapapeles usando tkinter
def get_video_url_from_clipboard():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    return root.clipboard_get()

# Función para seleccionar la carpeta donde guardar el archivo
def get_save_path():
    app = QApplication(sys.argv)
    # modifico para que guarde directamente en la carpeta indicada en vez de abrir dialogo
    save_path = "/home/dieg0nline/Downloads/Videos/"
    # save_path = QFileDialog.getExistingDirectory(None, 'Selecciona la carpeta donde guardar el archivo')
    if save_path:
        return save_path
    return None

# Main
if __name__ == '__main__':
    url = get_video_url_from_clipboard()
    if url:
        print(f"URL obtenida del portapapeles: {url}")
        save_path = get_save_path()
        if save_path:
            download_audio(url, save_path)
        else:
            print("No se seleccionó una carpeta de destino.")
    else:
        print("No se encontró una URL en el portapapeles.")
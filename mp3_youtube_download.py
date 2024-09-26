#!/usr/bin/env python3

import yt_dlp
import sys
import os
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from datetime import datetime
import dbus

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
        now = datetime.now().timestamp()
        os.utime(downloaded_file, (now, now))

    # Notificación final con un botón de cerrar
    send_notification("Descarga completada", "El archivo de audio ha sido guardado correctamente.", notification_id=notification_id, actions=["default", "Cerrar"])

# Función para descargar el video completo
def download_video(url, save_path):
    notification_id = send_notification("Descarga iniciada", "Iniciando descarga de video...")

    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d['_percent_str'].strip()
            speed = d['_speed_str'].strip()
            eta = d['_eta_str'].strip()
            message = f"Progreso: {percent}\nVelocidad: {speed}\nTiempo restante: {eta}"
            send_notification("Descargando video...", message, notification_id=notification_id)
        elif d['status'] == 'finished':
            send_notification("Descarga completada", "Video descargado correctamente.", notification_id=notification_id)

    # Opciones para la descarga de video
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook]  # Hook de progreso
    }

    # Descargar el archivo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Notificación final con un botón de cerrar
    send_notification("Descarga completada", "El video ha sido guardado correctamente.", notification_id=notification_id, actions=["default", "Cerrar"])

# Función para obtener la URL del portapapeles usando tkinter
def get_video_url_from_clipboard():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    return root.clipboard_get()

# Función para seleccionar la carpeta donde guardar el archivo
def get_save_path():
    save_path = "/home/dieg0nline/Downloads/Videos/"
    if save_path:
        return save_path
    return None

# Clase para la ventana emergente con botones
class DownloaderWindow(QWidget):
    def __init__(self, url, save_path):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Seleccionar Tipo de Descarga')
        layout = QHBoxLayout()

        # Botón para descargar el video completo
        video_button = QPushButton('Descargar Video Completo', self)
        video_button.clicked.connect(self.download_video)
        layout.addWidget(video_button)

        # Espacio entre los botones
        layout.addSpacing(10)

        # Botón para descargar solo el audio
        audio_button = QPushButton('Descargar Solo Audio', self)
        audio_button.clicked.connect(self.download_audio)
        layout.addWidget(audio_button)

        self.setLayout(layout)
        self.show()

    def download_video(self):
        download_video(self.url, self.save_path)
        QMessageBox.information(self, 'Descarga', 'El video completo se ha descargado con éxito.')
        self.close()

    def download_audio(self):
        download_audio(self.url, self.save_path)
        QMessageBox.information(self, 'Descarga', 'El audio se ha descargado con éxito.')
        self.close()

    # Sobrescribir el evento de cierre para salir completamente del programa
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Cerrar aplicación',
                                     "¿Seguro que quieres salir?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            QApplication.instance().quit()  # Salir completamente de la aplicación
        else:
            event.ignore()

# Main
if __name__ == '__main__':
    url = get_video_url_from_clipboard()
    if url:
        print(f"URL obtenida del portapapeles: {url}")
        save_path = get_save_path()
        if save_path:
            app = QApplication(sys.argv)
            ex = DownloaderWindow(url, save_path)
            sys.exit(app.exec_())
        else:
            print("No se seleccionó una carpeta de destino.")
    else:
        print("No se encontró una URL en el portapapeles.")

#!/usr/bin/env python3

import yt_dlp
import sys
import os
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QFileDialog
from datetime import datetime

# Función para descargar el audio en formato .mp3
def download_audio(url, save_path):
    # Modificar la plantilla del nombre de archivo
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Guardar en la carpeta seleccionada
    }

    # Descargar el archivo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url)
        downloaded_file = os.path.join(save_path, f"{info_dict['title']}.mp3")
    
    # Cambiar la fecha de modificación del archivo al día de hoy
    if os.path.exists(downloaded_file):
        now = datetime.now().timestamp()  # Obtener la marca de tiempo actual
        os.utime(downloaded_file, (now, now))  # Cambiar la fecha de acceso y modificación

# Función para obtener la URL del portapapeles usando tkinter
def get_video_url_from_clipboard():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    return root.clipboard_get()

# Función para seleccionar la carpeta donde guardar el archivo
def get_save_path():
    app = QApplication(sys.argv)
    # modifico para que guarde directamente en la carpeta indicada en vez de abrir dialogo
    # save_path = QFileDialog.getExistingDirectory(None, 'Selecciona la carpeta donde guardar el archivo')
    save_path = "/home/dieg0nline/Downloads/Videos/"
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
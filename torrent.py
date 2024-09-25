#!/usr/bin/env python3

import libtorrent as lt
import time
import tkinter as tk

# Función para obtener el magnet del portapapeles usando tkinter
def get_magnet_link_from_clipboard():
    root = tk.Tk()
    root.withdraw()
    return root.clipboard_get()

magnet_link = get_magnet_link_from_clipboard()


# Crear la sesión de BitTorrent
ses = lt.session()
params = {
    'save_path': '/home/dieg0nline/Downloads/',  # Carpeta donde se guardará el archivo descargado
    'storage_mode': lt.storage_mode_t.storage_mode_sparse
}

# Añadir el enlace magnet
handler = lt.add_magnet_uri(ses, magnet_link, params)

# Empezar la descarga
print("Descargando desde el enlace magnet...")
while not handler.is_seed():
    s = handler.status()
    print(f'Descargando: {s.progress * 100:.2f}% completado, Velocidad: {s.download_rate / 1000:.2f} kB/s')
    time.sleep(1)

print("Descarga completada.")
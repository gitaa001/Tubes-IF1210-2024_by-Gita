import os
import shutil
import time

# KUMPULAN PROSEDUR TAMBAHAN UNTUK USER INTERFACE

# Prosedur starter
def starter(*teks):
    '''Default Tampilan Program'''

    # teks = tampilan yang akan di masukkan sebagai starter
    os.system('cls')
    # Menulis kalimat pada starter
    for i in teks:
        print(i)
    
    # return 0

# Fungsi menu
def menu(*item:str) -> str:
    '''Menampilkan menu'''

    # Menampilkan pilihan menu
    for i in range(len(item)):
        print(f"{i+1}. {item[i]}")
    
    # Slot memilih menu
    jwb = input("\n>> Pilih: ")

    # RETURN
    return jwb

# Prosedur header
def print_centered_header(header):
    terminal_width = shutil.get_terminal_size().columns
    header_lines = header.split('\n')
    
    for line in header_lines:
        padding_left = (terminal_width - len(line)) // 2
        print(' ' * padding_left + line)

# Prosedur loading
def loading(*teks):
    # teks yg akan ditampilkan sebagai efek loading
    print(*teks)
    for i in range (2):
        print("")
        time.sleep(0.5)

import os
import argparse

# KUMPULAN PROSEDUR TAMBAHAN UNTUK USER INTERFACE

# Prosedur starter
def starter(*teks):
    '''Default Tampilan Program'''

    # KAMUS LOKAL
    # teks = tampilan yang akan di masukkan sebagai starter

    # ALGORITMA
    os.system('cls')
    # Menulis kalimat pada starter
    for i in teks:
        print(i)
    
    # return 0

# Fungsi menu
def menu(*item:str) -> str:
    '''Menampilkan menu'''

    # KAMUS LOKAL
    # item  = str pilihan 'button' pada menu
    # jwb   = str jawaban user

    # ALGORITMA
    # Menampilkan pilihan menu
    for i in range(len(item)):
        print(f"{i+1}. {item[i]}")
    
    # Slot memilih menu
    jwb = input("\n>> Pilih: ")

    # RETURN
    return jwb

# Prosedur split
def split(str, separator):
    hasil = []
    kata = ''
    for char in str:
        if char == separator:
            hasil.append(kata)
            kata = ''
        else:
            kata += char
    hasil.append(kata)
    return hasil

# Prosedur header
def print_centered_header(header):
    terminal_width = shutil.get_terminal_size().columns
    header_lines = header.split('\n')
    
    for line in header_lines:
        padding_left = (terminal_width - len(line)) // 2
        print(' ' * padding_left + line)

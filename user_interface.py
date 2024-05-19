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

# Prosedur read CSV
def data(nama):
    parser = argparse.ArgumentParser()
    parser.add_argument('Parent_Folder', metavar='folder', type=str, help='Masukkan Folder Penyimpanan')
    args = parser.parse_args()
    folder = args.Parent_Folder

    with open(f'{folder}/{nama}.csv', 'r') as file:
        data = file.read()
    rows=split(data,"\n")

    return rows
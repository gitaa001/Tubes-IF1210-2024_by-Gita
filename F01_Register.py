# SUBPROGRAM REGISTER

import os
import re
from user_interface import *

def is_valid_username(username):
    # Prosedur untuk memeriksa apakah username sesuai dengan kriteria
    pattern = r'^[a-zA-Z0-9_-]+$'
    return bool(re.match(pattern, username))

def register(user, monster, monster_inventory: dict) -> dict :

    # Prosedur untuk melakukan registrasi
    print("==== REGISTER ====\n")
    print("Selamat datang, Agent!\n")
    print("Silakan melakukan registrasi\n")

    # Validasi input username
    while True:
        username = input("Masukan username: ")
        password = input("Masukkan password: ")

        if is_valid_username(username):
            break
        else:
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip! \n")

        if username == user['username']:
            print('Register gagal!')
            print(f'Anda sudah log in dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali.')

    # Menampilkan pilihan monster
    for key, value in monster.items():
        print(f"{key}. {value['type']}")

    # ALGORITMA
    while True:
        # Slot memilih monster
        monster_choice = input(str("\n>> Monster pilihanmu: "))
        if monster_choice in monster:
            monster_user = monster[monster_choice]
            print(f"\nSelamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster_user['type']}!")
            break

        else:
            print("Pilihan tidak tersedia!")

    new_user_data = {
        'username': username, 
        'password': password, 
        'role'    : 'agent', 
        'oc'      : 0}
    
    new_user_id = str(len(user)+1)
    user[new_user_id] = new_user_data

    user_id = new_user_id
    user_data = new_user_data

    # ngetestttt
    # print(user)
    # print (user_id)
    # print(user_data)

    return user_id, user_data

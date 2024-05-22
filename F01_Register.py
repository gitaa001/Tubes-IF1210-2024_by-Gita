# SUBPROGRAM REGISTER

from user_interface import *
import re

def is_valid_username(username):
    # Prosedur untuk memeriksa apakah username sesuai dengan kriteria
    pattern = r'^[a-zA-Z0-9_-]+$'
    return bool(re.match(pattern, username))

def register(user, monster, monster_inventory, logged_in_user):
    # Prosedur untuk melakukan registrasi
    if logged_in_user:
        print(f"Register gagal!")
        print(f"Anda telah login dengan username {logged_in_user['username']}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
        return logged_in_user, user, monster_inventory

    starter("")
    print("\n========= REGISTER ===========\n")
    print("Selamat datang, Agent!\n")
    print("Silakan melakukan registrasi\n")

    # Validasi input username
    while True:
        username = input("Masukan username: ")
        password = input("Masukkan password: ")

        if username in [user[u]['username'] for u in user]:
            print(f"Username {username} sudah ada, silakan pilih username lain.\n")
            continue

        if not is_valid_username(username):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!\n")
            continue
        
        break

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
        'oc'      : '0'}

    new_user_id = str(len(user)+1)
    user[new_user_id] = new_user_data

    new_monster_inventory = {
        'monster_id': monster_choice,
        'level'     : '1'
    }

    if new_user_id in monster_inventory:
        monster_inventory[new_user_id].append(new_monster_inventory)
    else:
        monster_inventory[new_user_id] = [new_monster_inventory]

    return new_user_id, new_user_data, monster_inventory

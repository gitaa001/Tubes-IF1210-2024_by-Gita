from user_interface import *

# Function untuk mengecek apakah input integer atau bukan
def is_integer(s):
    digits = "0123456789"
    for char in s:
        if char not in digits:
            return False
    return True

# Function untuk menambahkan id monster baru
def newid(monster):
    max_id = -1
    for id in monster.keys():
        if int(id) > max_id:
            max_id = int(id)
    return max_id + 1

# Function untuk mengecek apakah monster baru sudah tersedia di database 'monster'
def dupecheck(name, monster):
    for id in monster:
        if monster[id]['type'].lower() == name.lower():
            return False
    return True

# Function untuk menambah monster baru ke dictionary
def tambah_monster_baru(monster, new_monster_data):
    new_id = str(len(monster) + 1)
    monster[new_id] = new_monster_data
    print("Monster baru telah ditambahkan!")
    return monster

# Fungsi utama F13
def monster_management(monster):
    starter("--------------------------------------------")
    print("\nSELAMAT DATANG DI DATABASE PARA MONSTER !!!")
    running = True  # Program akan berjalan selama running == True
    while running:
        print("\n Monster Management:")
        print("1. Tampilkan semua Monster")
        print("2. Tambah monster baru")
        print("3. Keluar")
        inp1 = input("\n>>> Pilih Aksi : ")
        if inp1 == '1':
            print("\nID | TYPE | ATK POWER | DEF POWER | HP ")
            for id, data in monster.items():
                type      = data['type']
                atk_power = data['atk_power']
                def_power = data['def_power']
                hp        = data['hp']
                print(f"{id} | {type} | {atk_power} | {def_power} | {hp} ")

        elif inp1 == '2':
            print("\n> Memulai pembuatan monster baru. . .")

            valid = False
            while not valid:
                new_monster = input("Masukkan Type/Nama : ")
                if not new_monster:
                    print("Masukkan input yang valid: ")
                elif not dupecheck(new_monster, monster):
                    print("Monster sudah terdaftar di database!")
                else:
                    valid = True

            valid2 = False
            while not valid2:
                atk_pow = input("Masukkan ATK Power : ")
                if not atk_pow or not is_integer(atk_pow):
                    print("Masukkan input bertipe Integer yang valid!\n")
                else:
                    valid2 = True

            valid3 = False
            while not valid3:
                def_pow = input("Masukkan DEF Power: ")
                if not def_pow or not is_integer(def_pow):
                    print("Masukkan input bertipe Integer yang valid!\n")
                elif not (0 <= int(def_pow) <= 50):
                    print("DEF Power harus bernilai 0-50, coba lagi!")
                else:
                    valid3 = True

            valid4 = False
            while not valid4:
                hp = input("Masukkan HP: ")
                if not hp or not is_integer(hp):
                    print("Masukkan input bertipe Integer yang valid!\n")
                else:
                    valid4 = True

            print("Name/Type   | ATK Power | DEF Power | HP")
            print(f"{new_monster} {' ' * (12 - len(new_monster))} | {atk_pow} {' ' * (10 - len(atk_pow))} | {def_pow} {' ' * (10 - len(def_pow))} | {hp}")

            inp2 = input("Tambahkan Monster ke Database (Y/N) : ")
            if inp2.lower() == 'y':
                new_monster_data = {"type": new_monster, "atk_power": int(atk_pow), "def_power": int(def_pow), "hp": int(hp)}
                monster = tambah_monster_baru(monster, new_monster_data)

        elif inp1 == '3':
            loading('Keluar...')
            running = False
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

    return monster

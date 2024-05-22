# ============ TEXT-BASED PYTHON GAME ===========
''' Mensimulasikan battle-game sederhana '''

# ================ IMPORT MODULE ================
import time
from user_interface import *
from F00_RandomGenerator import *
from F01_Register import *
from F02_Login import *
from F03_Logout import *
from F04_Help import *
from F07_inventory import *
from F08_Battle import *
from F09_Arena import *
from F10_Shop import *
from F11_Laboratory import *
from F12_ShopManagement import *
from F13_MonsterManagement import *
from F15_Save import *
from F16_Exit import *

# ============= Loading database ================
from F14_Load import *

# ============== Header Program =================
time.sleep(0.5)
print_centered_header(r"""
________________________________________________
                      
IRASSHAIMASE! Selamat Datang di Program
  ___      __    __       __       ____  __  __ 
 /   \    |  |__|  |     /  ]     /    ||  ||  |
|     |   |  |  |  |    /  /     |  o  ||  ||  |
|  O  |   |  |  |  |   /  /      |     ||__||__|
|     | __|  `  '  |__/   \_  __ |  _  | __  __ 
|     ||  |\      /|  \     ||  ||  |  ||  ||  |
 \___/ |__| \_/\_/ |__|\____||__||__|__||__||__|
________________________________________________
""")

# =========== Beberapa fungsi menu ==============
# AKSES KHUSUS AGENT
def menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop):
    islogin = True
    while islogin:
        print("\n======== MENU UTAMA =========")
        print(f"\n>>> Ohayou, Agent {user_data['username']}! Silakan pilih menu berikut:")

        pilih_aksi = menu("Battle: Bertarung melawan monster", "Arena: Tingkatkan kemampuan agent dengan latihan!", "Inventory: Lihat owca-dex yang kamu miliki", "Shop: Beli item baru", "Laboratory: Tingkatkan level monster", "Help", "Logout")
        if pilih_aksi == '1':
            user_data, item_inventory, monster = combat(user_id, user_data, monster, monster_inventory, item_inventory)

        elif pilih_aksi == '2':
            user_data, item_inventory, monster = main_arena(user_id, user_data, monster, monster_inventory, item_inventory)

        elif pilih_aksi == '3':
            inventory(user_id, user_data, monster, monster_inventory, item_inventory)

        elif pilih_aksi == '4':
            user_data, monster_inventory, item_inventory = main_shop(user_id, user_data, monster_shop, item_shop, monster, monster_inventory, item_inventory)
            
        elif pilih_aksi == '5':
            user_data, monster_inventory = laboratory(user_id, user_data, monster, monster_inventory)

        elif pilih_aksi == '6':
            help_as_agent(user_data)
            pilih = input("\n>>> Masukkan pilihan: ")
            if pilih.lower() == "logout":
               user_id, user_data = logging_out(user_id, user_data)
               return True  # Indikasi udah logout, user bisa login lagi

            if pilih.lower() == "menu":
                menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
                
        elif pilih_aksi == '7':
            user_id, user_data = logging_out(user_id, user_data)
            return True  # Indikasi udah logout, user bisa login lagi

        elif pilih_aksi.lower() == 'exit':
            exit_program(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
            break

        else: 
            print("Pilihan tidak tersedia.")

# AKSES KHUSUS ADMIN
def menu_admin(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop): 
    islogin = True
    while islogin:
        print("============= MENU ADMIN ==============")
        print(f"\nOhayou, Admin {user_data['username']}! Silakan pilih akses:")
        pilih_aksi = menu("Shop Management", "Monster Management", "Help", "Back")
        if pilih_aksi == '1':
            shop_management(user_data, monster, monster_shop, item_shop)

        elif pilih_aksi == '2':
            monster = monster_management(monster)

        elif pilih_aksi == '3':
            help_as_admin(user_id, user_data)
            pilih = input("\n>>> Masukkan pilihan: ")

            if pilih.lower() == "logout":
                user_id, user_data = logging_out(user_id, user_data)
                return True  
            
            if pilih.lower() == "shop":
                pilih_menu = menu("Shop Management", "Monster Management")
                if pilih_menu == '1':
                    monster_shop, item_shop = shop_management(user_data, monster, monster_shop, item_shop)
                if pilih_menu == '2':
                    monster = monster_management(monster)

            elif pilih_aksi.lower() == 'exit':
                exit_program(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
                break

# =============== Program Utama ================
while True:
    logged_in_user = None
    user_id = None
    user_data = None

    user_input = input("Ketik login untuk memulai atau help untuk meminta bantuan: ").lower()

    if user_input == 'login':
        user_id, user_data = login(user)
        logged_in_user = user_data  # Update logged_in_user dengan data pengguna yang login

        if user_id and user_data:
            if user_data['role'] == 'agent':
                logged_out = menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
                if logged_out:
                    logged_in_user = None  # Reset status login setelah logout
                    continue
            elif user_data['role'] == 'admin':
                logged_out = menu_admin(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
                if logged_out:
                    logged_in_user = None  # Reset status login setelah logout
                    continue

    elif user_input == 'help':
        help_before_login()
        pilih = input("\n>>> Masukkan pilihan: ").lower()
        if pilih == "register":
            user_id, user_data, monster_inventory = register(user, monster, monster_inventory, logged_in_user)
            if user_data and user_data['role'] == 'agent':
                logged_out = menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
                if logged_out:
                    logged_in_user = None  # Reset status login setelah logout
                    continue

        elif pilih == "login":
            user_id, user_data = login(user)
            if user_id and user_data:
                logged_in_user = user_data  # Update logged_in_user dengan data pengguna yang login
                if user_data['role'] == 'agent':
                    logged_out = menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
                    if logged_out:
                        logged_in_user = None  # Reset status login setelah logout
                        continue

    elif user_input.lower() == 'exit':
        exit_program(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
        break

    else:
        print("Pilihan tidak tersedia.")

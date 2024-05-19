# ============ TEXT-BASED PYTHON GAME ===========
''' Mensimulasikan battle-game sederhana '''

# ================ IMPORT MODULE ================
from user_interface import *
from F00_RandomGenerator import *
from F01_Register import *
from F02_Login import *
from F04_Help import *
from F07_inventory import *
from F08_Battle import *
from F09_Arena import *
from F10_Shop import *
from F11_Laboratory import *
from F12_ShopManagement import *
from F13_MonsterManagement import *
from F16_Logout import *

# ============= Loading database ================
from F14_Load import *

print(item_inventory)
print(item_shop)
# ============== Header Program =================
print("""
 _     _  _______  ___      _______  _______  __   __  _______ 
| | _ | ||       ||   |    |       ||       ||  |_|  ||       |
| || || ||    ___||   |    |       ||   _   ||       ||    ___|
|       ||   |___ |   |    |       ||  | |  ||       ||   |___ 
|       ||    ___||   |___ |      _||  |_|  ||       ||    ___|
|   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___ 
|__| |__||_______||_______||_______||_______||_|   |_||_______| 
""")

# =========== Beberapa fungsi menu ==============
def menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop): # Akses khusus agent
    print("\n======= MENU UTAMA =========")
    print("\n>>> Silakan pilih menu berikut:")
    while True:
        pilih_aksi = menu("Battle: Bertarung melawan monster", "Arena: Tingkatkan kemampuan agent dengan latihan!", "Inventory: Lihat owca-dex yang kamu miliki", "Shop: Beli item baru", "Laboratory: Tingkatkan level monster", "Help")
        if pilih_aksi == '1':
            user_data = combat(user_id, user_data, monster, monster_inventory, item_inventory)

        elif pilih_aksi == '2':
            battle_arena(user_id, user_data, monster, monster_inventory)
            break

        elif pilih_aksi == '3':
            inventory(user_id, user_data, monster, monster_inventory, item_inventory)
            break

        elif pilih_aksi == '4':
            monster_inventory, item_inventory = main_shop(user_data, monster_shop, item_shop, monster, monster_inventory, item_inventory)
 
        elif pilih_aksi == '5':
            user_data, monster_inventory = laboratory(user_id, user_data, monster, monster_inventory)

        elif pilih_aksi == '6':
            help_as_agent(user_data)
            pilih = input("\n>>> Masukkan pilihan: ")
            if pilih.lower() == "logout":
                import F16_Logout

            if pilih.lower() == "menu":
                menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)

            break

        else: 
            print("Pilihan tidak tersedia.")

def menu_admin(user_id, user_data, monster, monster_shop, item_shop): # Akses khusus admin
    print("\nSilakan pilih akses:")
    pilih_aksi = menu("Shop Management", "Monster Management", "Help", "Back")
    if pilih_aksi == '1':
        shop_management(user_data, monster, monster_shop, item_shop)

    elif pilih_aksi == '2':
        monster = monster_management(monster)

    elif pilih_aksi == '3':
        help_as_admin(user_id, user_data)
        pilih = input("\n>>> Masukkan pilihan: ")
        if pilih.lower() == "logout":
            import F16_Logout

        if pilih.lower() == "shop":
            pilih_menu = menu("Shop Management", "Monster Management")
            if pilih_menu == '1':
                monster_shop, item_shop = shop_management(user_data, monster, monster_shop, item_shop)
            if pilih_menu == '2':
                monster = monster_management(monster)

# =============== Program Utama =================
while True:
    # Menerima input awal user
    user_input = input("Ketik login untuk memulai atau help untuk meminta bantuan: ")
    user_input = user_input.lower()

    if user_input == 'login':
        user_id, user_data = login(user)
        if user_data['role'] == 'agent':
            menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)
        if user_data['role'] == 'admin':
            menu_admin(user_id, user_data, monster, monster_shop, item_shop)
        break

    if user_input == 'help':
        help_before_login()
        pilih = input("\n>>> Masukkan pilihan: ")
        if pilih.lower() == "register":
            user_id, user_data = register(user, monster, monster_inventory)
            if user_data['role'] == 'agent':
                menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)

    if pilih.lower() == "login":
        user_id, user_data = login(user)
        if user_id and user_data:
            menu_agent(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop)

        
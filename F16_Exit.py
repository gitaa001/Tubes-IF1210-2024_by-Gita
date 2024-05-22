import os
import sys
from F15_Save import *

def exit_program(user_id, user_data, monster, monster_inventory, item_inventory, monster_shop, item_shop):
    while True:
        choice = input(">>> Anda yakin ingin keluar dari program? (y/n): ")
        if choice.lower() == "y":
            save_confirmation = input("Apakah Anda ingin melakukan penyimpanan? (y/n): ")
            if save_confirmation.lower() == "y":
                folder = input("Nama Folder: ").strip()
                if folder:
                    userr_save(user_id, user_data, folder)
                    monster_save(monster, folder)
                    itemi_save(item_inventory, folder)
                    monsteri_save(monster_inventory, folder)
                    items_save(item_shop, folder)
                    monsters_save(monster_shop, folder)

                    print("File telah disimpan.")
                
                    if os.name == 'nt':
                        os.system('cls')

                    print(f"Anda akan keluar dari program. Sayonara Agent {user_data['username']}!")
                    sys.exit()  # Mengakhiri program

                else:
                    print("Nama folder tidak valid. Silakan coba lagi.")

            elif save_confirmation.lower() == "n":
                if os.name == 'nt':
                    os.system('cls')

                print(f"Anda akan keluar dari program. Sayonara Agent {user_data['username']}!")
                sys.exit()  # Mengakhiri program

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        elif choice.lower() == "n":
            print("Proses keluar dibatalkan.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

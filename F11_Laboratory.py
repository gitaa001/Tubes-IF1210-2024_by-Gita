def upgrade_monster(user_id, user_data, owca_coins, monsters, selected_monster_data, monster_inventory):
    selected_monster_id = selected_monster_data['monster_id']
    selected_monster = monsters[selected_monster_id]
    
    has_upgraded = False  # Variabel untuk menandai apakah upgrade telah dilakukan
    current_level = int(selected_monster_data['level'])
    while not has_upgraded:  # Melakukan upgrade hanya jika belum dilakukan sebelumnya
        if current_level >= 5:
            print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
            break
        else:
            upgrade_costs = [300, 500, 800, 1000]  # Daftar biaya upgrade untuk setiap level
            
            if current_level <= 4:
                upgrade_cost = upgrade_costs[current_level - 1]
                print(f"\n{selected_monster['type']} akan di-upgrade ke level {current_level + 1}.")
                print(f"Harga untuk melakukan upgrade {selected_monster['type']} adalah {upgrade_cost} OC.")
                
                if owca_coins >= upgrade_cost:
                    confirm = input("\n>>> Lanjutkan upgrade (Y/N): ")
                    if confirm in ['Y', 'y']:
                        current_level += 1
                        owca_coins -= upgrade_cost
                        print(f"Selamat, {selected_monster['type']} berhasil di-upgrade ke level {current_level}!")
                        has_upgraded = True  # Set variabel has_upgraded menjadi True setelah upgrade berhasil
                    elif confirm in ['N', 'n']:
                        print("Upgrade dibatalkan.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan masukkan Y atau N.")
                
                else:
                    print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.")
                    break
            else:
                print("Maaf, monster sudah mencapai level maksimum.")
                break

    # Update user_data dan monster_inventory
    user_data['oc'] = owca_coins
    selected_monster_data['level'] = str(current_level)
    return user_data, monster_inventory

def laboratory(user_id, user_data, monster, monster_inventory):
    while True:  
        print("\nSelamat datang di LAB DOKTER ASEP!!!\n")
        if user_id in monster_inventory:
            user_monsters = monster_inventory[user_id]
            
            print("======== MONSTER LIST =============")
            for i, monster_data in enumerate(user_monsters):
                monster_id = monster_data['monster_id']
                if monster_id in monster:
                    monster_details = monster[monster_id]
                    print(f"{i + 1}. {monster_details['type']} (Level: {monster_data['level']})")

        print("\n============ UPGRADE PRICE ============")
        print("1. Level 1 -> Level 2: 300 OC")
        print("2. Level 2 -> Level 3: 500 OC")
        print("3. Level 3 -> Level 4: 800 OC")
        print("4. Level 4 -> Level 5: 1000 OC")

        choice = input("\n>>> Pilih monster (atau ketik 'exit' untuk keluar): ")
        if choice == 'exit':
            return user_data, monster_inventory  # Return updated values when exiting
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(user_monsters):
                selected_monster_data = user_monsters[choice - 1]
                user_data, monster_inventory = upgrade_monster(user_id, user_data, int(user_data['oc']), monster, selected_monster_data, monster_inventory)
            else:
                print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")
        else:
            print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")


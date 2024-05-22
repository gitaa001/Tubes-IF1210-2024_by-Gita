from user_interface import *

def inventory(user_id, user_data, monster, monster_inventory, item_inventory):
    starter(f"\n========INVENTORY LIST (User ID: {user_id})=========")
    print(f"Jumlah OWCA Coin-mu sekarang: {user_data['oc']}")

    combined_list = [] # List untuk append item dalam 'monster_inventory' dan 'item_inventory'

    # Tambahkan monster ke combined_list
    if user_id in monster_inventory:
        for monster_data in monster_inventory[user_id]:
            monster_id = monster_data['monster_id']
            if monster_id in monster:
                monster_details = monster[monster_id]
                combined_list.append({
                    'type'      : 'monster',
                    'name'      : monster_details['type'],
                    'ATK Power' : monster_details['atk_power'],
                    'DEF Power' : monster_details['def_power'],
                    'hp'        : monster_details['hp'], 
                    'level'     : monster_data['level']})

    # Tambahkan potion ke combined_list
    if user_id in item_inventory:
        for item in item_inventory[user_id]:
            combined_list.append({
                'type'    : 'potion',
                'name'    : item['type'],
                'quantity': item['quantity'] })

    # Tampilkan inventory list
    count = 1
    for item in combined_list:
        if item['type'] == 'monster':
            print(f"{count}. Monster (Name: {item['name']}, Lvl: {item['level']}, HP: {item['hp']})")
        elif item['type'] == 'potion':
            print(f"{count}. Potion (Type: {item['name']}, Qty: {item['quantity']})")
        count += 1

    # Pilih item untuk menampilkan detail
    selected_item = None
    while True:
        pilihid = input("\n>>> Pilih nomor item untuk melihat detail atau ketik 'back' untuk kembali ke menu utama: ")
        
        if pilihid.isdigit():
            pilihid = int(pilihid)
            if 1 <= int(pilihid) <= len(combined_list):
                selected_item = combined_list[pilihid - 1]
                    # Menampilkan detail item yang dipilih
                if selected_item['type'] == 'monster':
                        print(f"\nDETAIL MONSTER")
                        print(f"Name       : {selected_item['name']}")
                        print(f"ATK Power  : {selected_item['ATK Power']}")
                        print(f"DEF Power  : {selected_item['DEF Power']}")
                        print(f"HP         : {selected_item['hp']}")
                        print(f"Level      : {selected_item['level']}")

                elif selected_item['type'] == 'potion':
                        print(f"\nDETAIL POTION")
                        print(f"Type    : {selected_item['name']}")
                        print(f"Quantity: {selected_item['quantity']}")

        elif pilihid.lower() == 'back':
            loading('Keluar...')
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan nomor item yang sesuai.")
            time.sleep(0.5)
            



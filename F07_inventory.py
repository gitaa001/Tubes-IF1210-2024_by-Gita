
# def inventory (user_id, user_data, monster, monster_inventory, item_inventory):
#     print(f"\n========INVENTORY LIST (User ID: {user_id})=========")
#     print(f"Jumlahh OWCA Coin-mu sekarang: {user_data['oc']}")

#     count = 1
#     if user_id in monster_inventory:
#         for monster_data in monster_inventory[user_id]:
#             monster_id = monster_data['monster_id']
#             if monster_id in monster:
#                 monster_details = monster[monster_id]
#                 print(f"{count}. Monster (Name: {monster_details['type']}, Lvl: {monster_data['level']}, HP: {monster[monster_id]['hp']})")
#                 count += 1
    
#     if user_id in item_inventory:
#         for item in item_inventory[user_id]:
#             print(f"{count}. Potion (Type: {item['type']}, Qty: {item['quantity']})")
#             count += 1
    
#     pilihid = input("\n>>> Ketikkan id untuk menampilkan detail item:")
#     if pilihid in monster_inventory:
#         print("Jenis item: MONSTER")
#         print("Name     :", monster_details['type'])
#         print("ATK Power:", monster_details['atk_power'])
#         print("DEF Power:", monster_details['def_power'])
#         print("HP       :", monster_details['hp'])
#         print("Level    :", monster_data['level'])

#     elif pilihid in item_inventory:
#         print("Jenis item: POTION")
#         print("Name     :", item['type'])
#         print("Quantity :", item['quantity'])

def inventory(user_id, user_data, monster, monster_inventory, item_inventory):
    print(f"\n========INVENTORY LIST (User ID: {user_id})=========")
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
        pilihid = int(input("\n>>> Pilih nomor item untuk melihat detail: "))
        if 1 <= pilihid <= len(combined_list):
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
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan nomor item yang sesuai.")



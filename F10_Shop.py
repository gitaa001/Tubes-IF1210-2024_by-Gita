from user_interface import *

# Fungsi untuk menampilkan item
def show_items(item_type, shop, monster):
    if item_type == 'monster':
        print("\nID | TYPE | ATK POWER | DEF POWER | HP | STOK | HARGA")
        for id, data in shop.items():
            stok = data['stock']
            harga = data['price']
            if id in monster:
                datamonster = monster[id]
                type        = datamonster['type']
                atk_power   = datamonster['atk_power']
                def_power   = datamonster['def_power']
                hp          = datamonster['hp']
                print(f"{id}  | {type} | {atk_power} | {def_power} | {hp} | {stok} | {harga}")
            else:
                print(f"Monster dengan ID {id} tidak ditemukan di database monster.")
    
    elif item_type == 'potion':
        print("\nID | TYPE | STOK | HARGA")
        for id, data in shop.items():
            type  = data['type']
            stok  = data['stock']
            harga = data['price']
            print(f'{id} | {type} | {stok} | {harga}')

    else:
        print("Tipe item tidak valid.")

# Fungsi untuk membeli item
def buy_item(user_id, shop, item_type, item_id, qty, oc, inventory, monster):
    if str(item_id) not in shop:
        print(f"Item dengan ID {item_id} tidak tersedia di shop.")
        return False

    item = shop[str(item_id)]

    # Validasi pembelian monster
    if item_type == "monster":
        if qty > 1:
            print("Hanya dapat membeli 1 monster sekaligus.")
            return False
        if oc < int(item["price"]):
            print("OC-mu tidak cukup.")
            return False
        # Validasi pembelian monster: cek apakah monster sudah ada di inventory
        if any(m["monster_id"] == str(item_id) for m in inventory['1']):
            print(f"Monster dengan ID {item_id} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
            return False
    
    # Validasi pembelian potion
    elif item_type == "potion":
        if oc < int(item["price"]) * qty:
            print("OC-mu tidak cukup.")
            return False
        if int(item["stock"]) < qty:
            print("Stok tidak mencukupi.")
            return False

    # Melakukan pembelian
    if item_type == "monster":
        print(f"Berhasil membeli monster: {monster[str(item_id)]['type']}. Monster sudah masuk ke inventory-mu!")
        item["stock"] = str(int(item["stock"]) - qty)
        inventory[user_id].append({'monster_id': str(item_id), 'level': '1'})

    else:
        print(f"Berhasil membeli {qty} {item['type']}. Item sudah masuk ke inventory-mu!")
        item["stock"] = str(int(item["stock"]) - qty)
        new_potion_qty = int(inventory[user_id][item_id]['quantity']) + qty
        inventory[user_id][item_id-1]['quantity'] = str(new_potion_qty)
        # item_id - 1 karena berupa list, sehingga indexing dr 0

    return True

# Main program
def main_shop(user_id, user_data, monster_shop, item_shop, monster, monster_inventory, item_inventory):
    oc = int(user_data['oc'])

    starter("-----------------------------------------------------")
    while True:
        print("\nIrasshaimase! Selamat datang dan selamat berbelanja!!")
        action = input(">>> Pilih aksi (lihat/beli/keluar): ").lower()

        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/potion): ").lower()
            if item_type == 'monster':
                shop = monster_shop
                show_items(item_type, shop, monster)
            elif item_type == 'potion':
                shop = item_shop
                show_items(item_type, shop, monster)

        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {oc}.")
            item_type = input(">>> Mau beli apa? (monster/potion): ").lower()
            if item_type == "monster":
                shop = monster_shop
                inventory = monster_inventory
                show_items(item_type, shop, monster)
                while True:
                    item_id = int(input(">>> Masukkan id monster: "))
                    if str(item_id) in shop:
                        break
                    else:
                        print("ID monster tidak tersedia. Silakan masukkan ID yang valid.")
                qty = 1
                
                success = buy_item(user_id, shop, item_type, item_id, qty, oc, inventory, monster)
                if success:
                    oc -= int(monster_shop[str(item_id)]["price"])

            elif item_type == "potion":
                shop = item_shop
                inventory = item_inventory
                show_items(item_type, shop, monster)
                while True:
                    item_id = int(input(">>> Masukkan id potion: "))
                    if str(item_id) in shop:
                        break
                    else:
                        print("ID potion tidak tersedia. Silakan masukkan ID yang valid.")
                qty = int(input(">>> Masukkan jumlah: "))
                success = buy_item(user_id, shop, item_type, item_id, qty, oc, inventory, monster)
                if success:
                    oc -= int(item_shop[str(item_id)]["price"]) * qty

            else:
                print("Tipe item tidak valid.")
                continue

            user_data['oc'] = str(oc)

        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            loading('Keluar...')
            break

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

    # print(monster_inventory)
    # print(item_inventory)
    return user_data, monster_inventory, item_inventory

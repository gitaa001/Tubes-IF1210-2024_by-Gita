# Fungsi untuk menampilkan item
def show_items(item_type, item_shop, monster_shop, monster):
    if item_type == 'monster':
        print("\nID | TYPE | ATK POWER | DEF POWER | HP | STOK | HARGA")
        for id, data in monster_shop.items():
            stok = data['stock']
            harga = data['price']
            if id in monster:
                datamonster = monster[id]
                type = datamonster['type']
                atk_power = datamonster['atk_power']
                def_power = datamonster['def_power']
                hp = datamonster['hp']
                print(f"{id} | {type} | {atk_power} | {def_power} | {hp} | {stok} | {harga}")
            else:
                print(f"Monster dengan ID {id} tidak ditemukan di database monster.")
    
    elif item_type == 'potion':
        print("\nID | TYPE | STOK | HARGA")
        for id, data in item_shop.items():
            type = data['type']
            stok = data['stock']
            harga = data['price']
            print(f'{id} | {type} | {stok} | {harga}')

    else:
        print("Tipe item tidak valid.")

# Fungsi untuk membeli item
def buy_item(user_id, shop, item_type, item_id, qty, oc, monster_inventory, item_inventory, monster):
    items = shop.get(item_type)
    if item_type == 'monster':
        items = shop
    
    if not items:
        print("Tipe item tidak valid.")
        return False

    item = items.get(str(item_id))
    if not item:
        print("Item tidak ditemukan.")
        return False

    # Validasi pembelian monster
    if item_type == "monster":
        if qty > 1:
            print("Hanya dapat membeli 1 monster sekaligus.")
            return False
        if oc < int(item["price"]):
            print("OC-mu tidak cukup.")
            return False
        # Validasi pembelian monster: cek apakah monster sudah ada di inventory
        if any(m["monster_id"] == str(item_id) for m in monster_inventory['1']):
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

    # Lakukan pembelian
    if item_type == "monster":
        print(f"Berhasil membeli monster: {monster[str(item_id)]['type']}. Monster sudah masuk ke inventory-mu!")
        item["stock"] = str(int(item["stock"]) - qty)
        monster_inventory[user_id].append({'monster_id': str(item_id), 'level': '1'})

    else:
        print(f"Berhasil membeli {qty} {item['type']}. Item sudah masuk ke inventory-mu!")
        item["stock"] = str(int(item["stock"]) - qty)
        item_inventory[user_id].append({'type': item['type'], 'quantity': str(qty)})

    
    return True

# Main program
def main_shop(user_id, user_data, monster_shop, item_shop, monster, monster_inventory, item_inventory):
    oc = int(user_data['oc'])

    while True:
        print("\nIrasshaimase! Selamat datang di SHOP!!")
        action = input(">>> Pilih aksi (lihat/beli/keluar): ").lower()

        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/potion): ").lower()
            show_items(item_type, item_shop, monster_shop, monster)

        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {oc}.")
            item_type = input(">>> Mau beli apa? (monster/potion): ").lower()
            if item_type == "monster":
                item_id = int(input(">>> Masukkan id monster: "))
                success = buy_item(user_id, monster_shop, item_type, item_id, 1, oc, monster_inventory, monster)
                if success:
                    oc -= int(monster_shop[str(item_id)]["price"])

            elif item_type == "potion":
                item_id = int(input(">>> Masukkan id potion: "))
                qty = int(input(">>> Masukkan jumlah: "))
                success = buy_item(user_id, item_shop, item_type, item_id, qty, oc, item_inventory)
                if success:
                    oc -= int(item_shop[str(item_id)]["price"]) * qty
            else:
                print("Tipe item tidak valid.")
                continue

        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
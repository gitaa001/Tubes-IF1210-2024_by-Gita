from F13_MonsterManagement import is_integer
item = {1:{'type': 'Strength'},2:{'type': 'Resilience'},3:{'type': 'Healing'}}
not_monster_shop = {}
not_item_shop = {}

def not_monster(monster, monster_shop):
    for id, data in monster.items():
        ada = False
        for idmonster, datamonster in monster_shop.items():
            if id == idmonster:
                ada = True
                break
        if not ada:
            type = data['type']
            atk_power = data['atk_power']
            def_power = data['def_power']
            hp        = data['hp']
            tidak_ada = {(id):{'type':(type),'atk_power':(atk_power),'def_power':(def_power),'hp':(hp)}}
            not_monster_shop.update(tidak_ada)
            
def not_item(item_shop):
    item = {1:{'type': 'Strength'},2:{'type': 'Resilience'},3:{'type': 'Healing'}}
    for id, data in item.items():
        ada = False
        for iditem, dataitem in item_shop.items():
            if id == iditem:
                ada = True
                break
        if not ada:
            type = data['type']
            tidak_ada = {(id):{'type': (type)}}
            not_item_shop.update(tidak_ada)

def tampilkan_shop(barang, monster_shop, monster, item_shop):
    if barang == 'monster':
        print("\nID | TYPE | ATK POWER | DEF POWER | HP | STOK | HARGA")
        for id, data in monster_shop.items():
            stok = data['stock']
            harga = data['price']
            for idmonster, datamonster in monster.items():
                if idmonster == id:
                    type      = datamonster['type']
                    atk_power = datamonster['atk_power']
                    def_power = datamonster['def_power']
                    hp = datamonster['hp']
            print(f"{id} | {type} | {atk_power} | {def_power} | {hp} | {stok} | {harga}")
    
    elif barang == 'item':
        print("\nID | TYPE | STOK | HARGA")
        for id, data in item_shop.items():
            type  = data['type']
            stok  = data['stock']
            harga = data['price']
            print(f'{id} | {type} | {stok} | {harga}')

def shop_management(user_data, monster, monster_shop, item_shop):
    print(f'========== SELAMAT DATANG, MR. {user_data["username"]} ==========')
    if user_data['role'] == 'admin':
        while True:
            aksi = input('\nPilih aksi (lihat/tambah/ubah/hapus/keluar): ').lower()

            if aksi == 'lihat':
                sub_aksi = input('\nApa yang mau dilihat? (monster/item): ').lower()
                if sub_aksi == 'monster':                   
                    tampilkan_shop(sub_aksi, monster_shop, monster, item_shop)
                elif sub_aksi == 'item':
                    tampilkan_shop(sub_aksi, monster_shop, monster, item_shop)
                else:
                    print("Pilihan tidak tersedia!")

            elif aksi == 'tambah':
                sub_aksi = input('\nApa yang mau ditambah? (monster/item): ').lower()
                if sub_aksi == 'monster':
                    print('ID | TYPE | ATK POWER | DEF POWER | HP')
                    not_monster(monster, monster_shop)
                    
                    for id, data in not_monster_shop.items():
                        type      = data['type']
                        atk_power = data['atk_power']
                        def_power = data['def_power']
                        hp        = data['hp']
                        print(f'{id} | {type} | {atk_power} | {atk_power} | {def_power} | {hp}')    

                    id_monster = input("\nMasukkan ID Monster: ")
                    stok = input("Masukkan Stok Awal: ")
                    harga = input("Masukkan Harga: ")

                    if is_integer(stok) and is_integer(harga) and is_integer(id_monster):
                        for id, data in not_monster_shop.items():
                            if id_monster == id:
                                tambah = {(id):{'stock': (stok), 'price': (harga)}}
                                monster_shop.update(tambah)
                                print('\nITEM BERHASIL DITAMBAHKAN KE SHOP')
                    else:
                        print("Inputan harus berupa integer!")


                elif sub_aksi == 'item':
                    print('ID | TYPE')
                    not_item(item_shop) # Adjust as needed
                    for id, data in not_item_shop.items():
                        type = data['type']
                        print(f'{id} | {type}')

                    id_item = input('\nMasukkan ID Item: ')
                    stok    = input('Masukkan Stok Awal: ')
                    harga   = input('Masukkan Harga: ')

                    if is_integer(id_item) and is_integer(stok) and is_integer(harga):
                        for id, data in not_item_shop.items():
                            if id_item == id:
                                type   = data['type']
                                tambah = {(id):{'type': (type), 'stock': (stok), 'price': (harga)}}
                                item_shop.update(tambah)
                                print('\nITEM BERHASIL DITAMBAHKAN KE SHOP')
                                break
                    else:
                        print("Inputan harus berupa integer!")

            elif aksi == 'ubah':
                sub_aksi = input('\nApa yang mau diubah? (monster/item): ').lower()
                if sub_aksi == 'monster':
                    tampilkan_shop(sub_aksi, monster_shop, monster, item_shop)

                    id = input("\nMasukkan ID Monster: ")
                    stok = input("Masukkan Stok Baru: ")
                    harga = input("Masukkan Harga Baru: ")

                    if is_integer(id) and is_integer(stok) and is_integer(harga):
                        if stok:
                            monster_shop[id]['stock'] = stok
                        if harga:
                            monster_shop[id]['price'] = harga

                        if stok and harga:
                            print(f"Monster telah berhasil diubah dengan stok baru sejumlah {stok} dan dengan harga baru {harga}")
                        elif stok:
                            print(f"Monster telah berhasil diubah dengan stok baru sejumlah {stok}")
                        elif harga:
                            print(f"Monster telah berhasil diubah dengan harga baru {harga}")
                        else:
                            print("Isi Stok/Harga yang ingin diubah")
                    else:
                        print("Inputan harus berupa integer!")

                elif sub_aksi == 'item':
                    tampilkan_shop(sub_aksi, monster_shop, monster, item_shop)

                    id = input("\nMasukkan ID Item: ")
                    stok = input("Masukkan Stok Baru: ")
                    harga = input("Masukkan Harga Baru: ")

                    if is_integer(id) and is_integer(stok) and is_integer(harga):
                        if stok:
                            item_shop[id]['stock'] = stok
                        if harga:
                            item_shop[id]['price'] = harga

                        if stok and harga:
                            print(f"Item telah berhasil diubah dengan stok baru sejumlah {stok} dan dengan harga baru {harga}")
                        elif stok:
                            print(f"Item telah berhasil diubah dengan stok baru sejumlah {stok}")
                        elif harga:
                            print(f"Item telah berhasil diubah dengan harga baru {harga}")
                        else:
                            print("Isi Stok/Harga yang ingin diubah")
                    print("Inputan harus berupa integer!")

            elif aksi == 'hapus':
                sub_aksi = input('\nApa yang mau dihapus? (monster/item): ').lower()
                if sub_aksi == 'monster':          
                    tampilkan_shop(sub_aksi, monster_shop, monster, item_shop)

                    id = input("\nMasukkan ID Monster: ")
                    if is_integer(id):
                        confirm = input('Apakah anda yakin ingin menghapus Monster dari shop (y/n)? ').lower()
                        
                        if confirm == 'y':
                            del monster_shop[id]
                            print("Monster berhasil dihapus dari shop")
                        else:
                            print("Penghapusan dibatalkan")
                    else:
                        print("Inputan harus berupa integer!")

                elif sub_aksi == 'item':
                    tampilkan_shop(sub_aksi, monster_shop, monster, item_shop)

                    id = input("\nMasukkan ID Item: ")
                    if is_integer(id):
                        confirm = input('Apakah anda yakin ingin menghapus Item dari shop (y/n)? ').lower()
                        
                        if confirm == 'y':
                            del item_shop[id]
                            print("Item berhasil dihapus dari shop")
                        else:
                            print("Penghapusan dibatalkan")
                    else:
                        print("Inputan harus berupa integer!")

            elif aksi == 'keluar':
                print('Dadah Mr. Monogram!')
                break

            else:
                print("Pilihan tidak tersedia! Silakan coba lagi.")

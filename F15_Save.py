import os

def folder_check(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"The new folder {folder} has been created!")
    else:
        print(f"Folder {folder} already exists.")

def save(data, folder, filename, header, keys):
    folder_check(folder)  # Pastikan folder ada sebelum menyimpan
    with open(f"{folder}/{filename}", 'w') as file:
        file.write(','.join(header) + '\n')
        for key, items in data.items():
            for item in items:
                if isinstance(item, dict):
                    row = [key] + [str(item.get(k, '')) for k in keys]
                    file.write(','.join(row) + '\n')

def userr_save(user_id, user_data, folder):
    data = {user_id: [user_data]}
    filename = "user.csv"
    header = ['id', 'username', 'password', 'role', 'oc']
    keys = header[1:]
    save(data, folder, filename, header, keys)

def monster_save(monster, folder):
    data = monster
    filename = "monster.csv"
    header = ['id', 'type', 'atk_power', 'def_power', 'hp']
    keys = header[1:]
    save(data, folder, filename, header, keys)

def itemi_save(item_inventory, folder):
    data = item_inventory
    filename = "item_inventory.csv"
    header = ['user_id', 'type', 'quantity']
    keys = header[1:]
    save(data, folder, filename, header, keys)

def monsteri_save(monster_inventory, folder):
    data = monster_inventory
    filename = "monster_inventory.csv"
    header = ['user_id', 'monster_id', 'level']
    keys = header[1:]
    save(data, folder, filename, header, keys)

def items_save(item_shop, folder):
    data = item_shop
    filename = "item_shop.csv"
    header = ['id', 'type', 'stock', 'price']
    keys = header[1:]
    save(data, folder, filename, header, keys)

def monsters_save(monster_shop, folder):
    data = monster_shop
    filename = "monster_shop.csv"
    header = ['monster_id', 'stock', 'price']
    keys = header[1:]
    save(data, folder, filename, header, keys)

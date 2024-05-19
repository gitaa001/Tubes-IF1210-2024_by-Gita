import F14_Load
import os

folder = "my_folder"


data = F14_Load.monster_inventory

folder=input("Nama Folder: ")

def folder_check(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"The new folder {folder} has been created!")

def save(data, folder, filename, header, keys):
    with open(f"{folder}/{filename}", 'w') as file:
        file.write(','.join(header) + '\n')
        for key in data:
            for item in data[key]:
                row = [key] + [item[k] for k in keys]
                file.write(str(key) + ',' + ','.join(str(x) for x in row[1:]) + '\n')

def userr():
    global folder
    data = F14_Load.user
    filename = "user.csv"
    header = ['id','username','password','role','oc']
    keys = []
    for i in range (1, len(header)):
        keys.append(header[i])
    # save(data,folder,filename,header,keys)

def monsterr():
    global folder
    data = F14_Load.monster
    filename = "monster.csv"
    header = ['id','type','atk_power','def_power','hp']
    keys = []
    for i in range (1, len(header)):
        keys.append(header[i])
    # save(data,folder,filename,header,keys)

def itemi():
    global folder
    data = F14_Load.item_inventory
    filename = "item_inventory.csv"
    header = ['user_id','type','quantity']
    keys = []
    for i in range (1, len(header)):
        keys.append(header[i])
    # save(data,folder,filename,header,keys)

def monsteri():
    global folder
    data = F14_Load.monster_inventory
    filename = "monster_inventory.csv"
    header = ['user_id','monster_id','level']
    keys = []
    for i in range (1, len(header)):
        keys.append(header[i])
    # save(data,folder,filename,header,keys)

def items():
    global folder
    data = F14_Load.item_shop
    filename = "item_shop.csv"
    header = ['id','type','stock','price']
    keys = []
    for i in range (1, len(header)):
        keys.append(header[i])
    # save(data,folder,filename,header,keys)

def monsters():
    global folder
    data = F14_Load.monster_shop
    filename = "monster_shop.csv"
    header = ['monster_id','stock','price']
    keys = []
    for i in range (1, len(header)):
        keys.append(header[i])
    # save(data,folder,filename,header,keys)

# folder_check(folder)
# userr()
# monsterr()
# itemi()
# monsteri()
# items()
# monsters()

# header = ['user_id', 'monster_id', 'level']
# keys = ['monster_id', 'level']
# write_dict_to_csv(data, 'output2.csv', header, keys)

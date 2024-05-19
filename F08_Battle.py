from F00_RandomGenerator import *
from user_interface import *

# ---------- Skema battle -----------

def calculate_damage(attack, defense):
    base_damage = attack 
    modified_damage = float(base_damage) - (float(base_damage) * (float(defense) / 100))  # Modify damage based on enemy defense
    return modified_damage

def take_damage(character, damage):
    sisa_hp = float(character['hp'])
    sisa_hp -= damage
    if sisa_hp < 0:
        sisa_hp = 0
    
    # Update HP monster dalam dictionary 'monster'
    character['hp'] = sisa_hp

    print(f"Name      : {character['type']}")
    print(f"ATK Power : {character['atk_power']}")
    print(f"DEF Power : {character['def_power']}")
    print(f"HP        : {character['hp']}")
    print(f"Level     : {1}")

def player_attack(player, enemy):
    damage_dealt = calculate_damage(player['atk_power'], enemy['def_power'])
    print(f"SCHWINKKK, {player['type']} menyerang {enemy['type']} !!!")
    take_damage(enemy, damage_dealt)
    print(f"# Penjelasan: ATT: {damage_dealt}, Reduced by: {enemy['def_power']}%, ATT Results: {damage_dealt}")
    return enemy['hp'] == 0

def enemy_attack(enemy, player):
    damage_dealt = calculate_damage(enemy['atk_power'], player['def_power'])
    print(f"SCHWINKKK, {enemy['type']} menyerang {player['type']} !!!")
    take_damage(player, damage_dealt)
    print(f"# Penjelasan: ATT: {damage_dealt}, Reduced by: {player['def_power']}%, ATT Results: {damage_dealt}")
    return player['hp'] == 0

# ------- Pilih monster untuk battle --------
def display_user_monsters(user_id, monster_inventory, monster):
    # Cek apakah user memiliki monster dalam inventory
    if user_id in monster_inventory:
        user_monsters = monster_inventory[user_id]
        
        print("\n======== MONSTER LIST =============")
        print("Pilih monster untuk bertarung")
        
        for i, monster_data in enumerate(user_monsters):
            monster_id = monster_data['monster_id']
            if monster_id in monster:
                monster_details = monster[monster_id]
                print(f"{i + 1}. {monster_details['type']} (Level: {monster_data['level']})")
    else:
        print("Kamu tidak memiliki monster dalam inventory!")

# ----- Main Program Battle -----------
def combat(user_id, user_data, monster, monster_inventory, item_inventory):
    # Randomize monster musuh dengan LCG
    RNG_monster = interval(1, len(monster))
    key = str(RNG_monster)

    lvl_monster = interval(1, 5)

    # Menampilkan spesifikasi monster musuh
    enemy           = monster[key]
    Nama_monster    = enemy['type']
    ATK_monster     = enemy["atk_power"]
    DEF_monster     = enemy["def_power"]
    HP_monster      = enemy["hp"]
    Level           = lvl_monster
    if lvl_monster == 1:
        ATK_monster == int(enemy["atk_power"]) * 1
    elif lvl_monster == 2:
        ATK_monster == int(enemy["atk_power"]) * 2 
    elif lvl_monster == 3:
        ATK_monster == int(enemy["atk_power"]) * 3
    elif lvl_monster == 1:
        ATK_monster == int(enemy["atk_power"]) * 4
    elif lvl_monster == 1:
        ATK_monster == int(enemy["atk_power"]) * 5

    print("\n _______ SELAMAT DATANG DI BATTLE!!! _______")
    print(r"""
           _/\----/\   
          /         \     /\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__
""")
    print(f"RAWRRR, Monster {Nama_monster} telah muncul !!!")
    print("Nama       :", Nama_monster)
    print("ATK power  :", ATK_monster)
    print("DEF power  :", DEF_monster)
    print("HP         :", HP_monster)
    print("Level      :", Level)

    # Menampilkan pilihan monster player sesuai kepemilikan di 'monster_inventory'
    display_user_monsters(user_id, monster_inventory, monster)

    while True:
        pilih_monster = input(str(">> Pilih monster untuk bertarung: "))
        player = monster[pilih_monster]
        player_level = monster_inventory[user_id][int(pilih_monster)-1]['level']
        if pilih_monster in monster:
            print(r'''
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 
''')
            print(f"RAWRRR, Agent {user_data['username']} mengeluarkan monster {player['type']}!!!")
            print("Nama       :", player['type'])
            print("ATK power  :", player['atk_power'])
            print("DEF power  :", player['def_power'])
            print("HP         :", player['hp'])
            print(f"Level     :", player_level) 
              
            # Skema 1V1 turn-based battle
            turn = 1
            while int(player['hp']) > 0 and int(enemy['hp']) > 0:
                    
                    # Update ATK monster musuh sesuai level

                    print(f"============ TURN {turn} ({player['type']}) ============")
                    pilih = menu("Attack", "Use Potion", "Quit")

                    if pilih == '1':
                        if player_attack(player, enemy):
                            # Check apakah enemy telah dikalahkan
                            print(f"\nSelamat, Anda berhasil mengalahkan monster {enemy['type']} !!!\n")

                            OC_reward = interval(10, 100) # Perolehan hadiah OC
                            print(f"Total OC yang diperoleh: {OC_reward}\n")

                            # Update jumlah OC dalam dictionary 'user'
                            owca_coin = int(user_data['oc']) + OC_reward
                            user_data['oc'] = str(owca_coin)
                            print(user_data)
                            return user_data

                    elif pilih == '2':
                        print("========POTION LIST===========")

                        potion_used = [] # List kosong untuk menampung potion yg telah dipakai
                        while True:
                            item_user = item_inventory[user_id]
                            sisa_potion1 = int(item_user[0]['quantity'])
                            sisa_potion2 = int(item_user[1]['quantity'])
                            sisa_potion3 = int(item_user[2]['quantity'])

                            print(f"1. {item_user[0]} (Qty: {sisa_potion1})")
                            print(f"2. {item_user[1]} (Qty: {sisa_potion2})")
                            print(f"3. {item_user[2]} (Qty: {sisa_potion3})")
                            print("4. Cancel")

                            perintah = input(">>> Pilih perintah: \n")

                            if perintah == '1':
                                if sisa_potion1 > 0:
                                    if perintah in potion_used:
                                        print('''Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia 
                                                menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.''')
                                    else:
                                            print('''Setelah meminum ramuan ini, aura kekuatan terlihat 
                                            mengelilingi Pikachow dan gerakannya menjadi lebih cepat dan mematikan.''')
                                            attack = (0.05 * float(player['atk_power'])) + float(player['atk_power'])
                                            player_attack(player, enemy)
                                            sisa_potion1 -= 1
                                            potion_used.append('1') # Potion 1 telah dipakai
                                else:
                                    print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                                    continue

                            elif perintah == '2':
                                    if sisa_potion2 > 0:
                                        if perintah in potion_used:
                                            print('''Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia 
                                                menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.''')
                                        else: 
                                            print('''Setelah meminum ramuan ini, muncul sebuah energi pelindung di 
                                            sekitar Pikachow yang membuatnya terlihat semakin tangguh dan sulit dilukai.''')
                                            defense = (0.05 * float(player['def_power'])) + float(player['def_power'])
                                            player_attack(player, enemy)
                                            sisa_potion2 -= 1
                                            potion_used.append('2') # Potion 2 telah dipakai
                                    else:
                                        print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                                        continue

                            elif perintah == '3':
                                    if sisa_potion3 > 0:
                                        if perintah in potion_used:
                                            print('''Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia 
                                                menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.''')
                                        else:     
                                            print('''Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh Pikachow sembuh
                                            dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.''')
                                            sisa_hp = (0.25 * float(player['hp'])) + float(player['hp'])
                                            player_attack(player, enemy)
                                            sisa_potion3 -= 1
                                            potion_used.append('3') # Potion 3 telah dipakai
                                    else:
                                        print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                                        continue

                            else:
                                print("Item tidak tersedia!!!")

                            # Update quantity potion dalam dictionary 'item_inventory'
                            item_user[0]['quantity'] = sisa_potion1
                            item_user[1]['quantity'] = sisa_potion2
                            item_user[2]['quantity'] = sisa_potion3

                            break

                    elif pilih == '3':
                        print("Anda berhasil kabur dari BATTLE!")
                        return user_data

                    else:
                        print("Pilihan tidak tersedia!")

                    print(f"============ TURN {turn} ({enemy['type']}) ============")
                    if enemy_attack(enemy, player):
                        print(f"\nYahhh, Anda dikalahkan monster {enemy['type']}. Jangan menyerah, coba lagi !!!\n")
                        print(user_data)
                        return user_data

                    turn += 1

        else:
            print("Pilihan nomor tidak tersedia!")

        

          
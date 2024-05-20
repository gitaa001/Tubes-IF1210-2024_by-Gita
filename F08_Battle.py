from F00_RandomGenerator import *
from user_interface import *

# ------------ Efek Potion --------------
def efek_potion(potion_effects, player):
    attack  = int(player['atk_power'])
    defense = int(player['def_power'])
    hp      = int(player['hp'])

    if potion_effects == 'strength':
       attack = (0.05 * int(player['atk_power'])) + int(player['atk_power'])
    
    if potion_effects == 'resilience':
       defense = (0.05 * int(player['def_power'])) + int(player['def_power'])

    if potion_effects == 'healing':
       hp = (0.25 * int(player['hp'])) + int(player['hp'])

    return attack, defense, hp

# ------------ Stat Menurut Level --------------
def upgrade_stat(character, level):
    if level == '1':
        ATK_power = int(character["atk_power"]) 
        DEF_power = int(character["def_power"]) 
        HP_power  = int(character["hp"]) 
    elif level == '2':
        ATK_power = int(character["atk_power"]) + 5
        DEF_power = int(character["def_power"]) + 20
        HP_power  = int(character["hp"]) + 20
    elif level == '3':
        ATK_power = int(character["atk_power"]) + 10
        DEF_power = int(character["def_power"]) + 30
        HP_power  = int(character["hp"]) + 30
    elif level == '4':
        ATK_power = int(character["atk_power"]) + 15
        DEF_power = int(character["def_power"]) + 40
        HP_power  = int(character["hp"]) + 40
    elif level == '5':
        ATK_power = int(character["atk_power"]) + 20
        DEF_power = int(character["def_power"]) + 50
        HP_power  = int(character["hp"]) + 50

    return ATK_power, DEF_power, HP_power

# ------------ Skema battle --------------
def calculate_damage(attack, defense):
    base_damage = attack 
    modified_damage = float(base_damage) - (float(base_damage) * (float(defense) / 100))  # Modify damage based on enemy defense
    return modified_damage

def take_damage_monster(character, damage, level):
    sisa_hp = float(character['hp']) - damage
    if sisa_hp < 0:
        sisa_hp = 0
    
    # Update HP monster dalam dictionary 'monster'
    character['hp'] = sisa_hp

    print(f"Name      : {character['type']}")
    print(f"ATK Power : {character['atk_power']}")
    print(f"DEF Power : {character['def_power']}")
    print(f"HP        : {character['hp']}")
    print(f"Level     : {level}")

def take_damage_player(character, damage, level):
    sisa_hp = float(character['hp']) - damage
    if sisa_hp < 0:
        sisa_hp = 0
    
    # Update HP monster dalam dictionary 'monster'
    character['hp'] = sisa_hp

    print(f"Name      : {character['type']}")
    print(f"ATK Power : {character['atk_power']}")
    print(f"DEF Power : {character['def_power']}")
    print(f"HP        : {character['hp']}")
    print(f"Level     : {level}")


def player_attack(player, enemy, level):
    damage_dealt = calculate_damage(player['atk_power'], enemy['def_power'])
    print(f"SCHWINKKK, {player['type']} menyerang {enemy['type']} !!!")
    take_damage_monster(enemy, damage_dealt, level)
    print(f"# Penjelasan: ATT: {damage_dealt}, Reduced by: {enemy['def_power']}%, ATT Results: {damage_dealt}")
    return enemy['hp'] == 0

def enemy_attack(enemy, player, level):
    damage_dealt = calculate_damage(enemy['atk_power'], player['def_power'])
    print(f"SCHWINKKK, {enemy['type']} menyerang {player['type']} !!!")
    take_damage_player(player, damage_dealt, level)
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
    initial_enemy_hp = enemy['hp']

    # Randomize monster musuh dengan LCG
    RNG_monster = interval(1, len(monster))
    key = str(RNG_monster)

    lvl_monster = str(interval(1, 5))    
    enemy       = monster[key]
    enemy['atk_power'], enemy['def_power'], enemy['hp'] = upgrade_stat(enemy, lvl_monster)

    # Menampilkan spesifikasi monster musuh
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
    print(f"RAWRRR, Monster {enemy['type']} telah muncul !!!")
    print("Nama       :", enemy['type'])
    print("ATK power  :", enemy['atk_power'])
    print("DEF power  :", enemy['def_power'])
    print("HP         :", enemy['hp'])
    print("Level      :", lvl_monster)

    # Menampilkan pilihan monster player sesuai kepemilikan di 'monster_inventory'
    display_user_monsters(user_id, monster_inventory, monster)

    while True:
        pilih_monster = input(str(">> Pilih monster untuk bertarung: "))
        player = monster[pilih_monster]
        initial_player_hp = player['hp']
        player_level = monster_inventory[user_id][int(pilih_monster)-1]['level']
        player['atk_power'], player['def_power'], player['hp']= upgrade_stat(player, player_level)
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
            potion_used = [False, False, False] # List untuk validasi potion yg telah dipakai
            while int(player['hp']) > 0 and int(enemy['hp']) > 0:
                    print(f"============ TURN {turn} ({player['type']}) ============")
                    pilih = menu("Attack", "Use Potion", "Quit")

                    if pilih == '1':
                        if player_attack(player, enemy, player_level):
                            # Check apakah enemy telah dikalahkan
                            print(f"\nSelamat, Anda berhasil mengalahkan monster {enemy['type']} !!!\n")

                            OC_reward = interval(10, 100) # Perolehan hadiah OC
                            print(f"Total OC yang diperoleh: {OC_reward}\n")

                            # Update jumlah OC dalam dictionary 'user'
                            owca_coin = int(user_data['oc']) + OC_reward
                            user_data['oc'] = str(owca_coin)
                            
                            return user_data, item_inventory

                    elif pilih == '2':
                        print("========POTION LIST===========")
                        
                        while True:
                            item_user = item_inventory[user_id]
                            sisa_potion1 = int(item_user[0]['quantity'])
                            sisa_potion2 = int(item_user[1]['quantity'])
                            sisa_potion3 = int(item_user[2]['quantity'])

                            while True:
                                print(f"1. Strength Potion (Qty: {sisa_potion1}) - Increases ATK Power")
                                print(f"2. Resilience Potion (Qty: {sisa_potion2}) - Increases DEF Power")
                                print(f"3. Healing Potion (Qty: {sisa_potion3}) - Restores Health")
                                print("4. Cancel")

                                perintah = input(">>> Pilih perintah: \n")

                                if perintah == '1':
                                    if sisa_potion1 > 0:
                                        if potion_used[0]:
                                            print('''Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia 
    menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.''')
                                        else:
                                            print('''Setelah meminum ramuan ini, aura kekuatan terlihat 
    mengelilingi Pikachow dan gerakannya menjadi lebih cepat dan mematikan.''')
                                            potion_effects = efek_potion('strength', player)
                                            player['atk_power'] = potion_effects[0]
                                            sisa_potion1 -= 1
                                            potion_used[0] = True # Potion 1 telah dipakai
                                            break
                                            
                                    else:
                                        print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                                        continue

                                elif perintah == '2':
                                    if sisa_potion2 > 0:
                                        if potion_used[1]:
                                            print('''Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia 
    menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.''')
                                        else: 
                                            print('''Setelah meminum ramuan ini, muncul sebuah energi pelindung di 
    sekitar Pikachow yang membuatnya terlihat semakin tangguh dan sulit dilukai.''')
                                            potion_effects = efek_potion('resilience', player)
                                            player['def_power'] = potion_effects[1]
                                            sisa_potion2 -= 1
                                            potion_used[1] = True # Potion 2 telah dipakai
                                            break
                                            
                                    else:
                                        print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                                        continue

                                elif perintah == '3':
                                    if sisa_potion3 > 0:
                                        if potion_used[2]:
                                            print('''Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia 
menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.''')
                                        else:     
                                            print('''Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh Pikachow sembuh
dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.''')
                                            potion_effects = efek_potion('healing', player)
                                            player['hp'] = potion_effects[2]
                                            sisa_potion3 -= 1
                                            potion_used[2] = True # Potion 3 telah dipakai
                                            break
                                            
                                    else:
                                        print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                                        continue

                                elif perintah == '4':
                                    break

                                else:
                                    print("Item tidak tersedia!!!")

                            # Update quantity potion dalam dictionary 'item_inventory'
                            item_user[0]['quantity'] = sisa_potion1
                            item_user[1]['quantity'] = sisa_potion2
                            item_user[2]['quantity'] = sisa_potion3
                            item_inventory[user_id] = item_user

                            break

                    elif pilih == '3':
                        print("Anda berhasil kabur dari BATTLE!")
                        return user_data, item_inventory

                    else:
                        print("Pilihan tidak tersedia!")

                    print(f"============ TURN {turn} ({enemy['type']}) ============")
                    if enemy_attack(enemy, player, lvl_monster):
                        print(f"\nYahhh, Anda dikalahkan monster {enemy['type']}. Jangan menyerah, coba lagi !!!\n")
                   
                        return user_data, item_inventory

                    turn += 1

        else:
            print("Pilihan nomor tidak tersedia!")
    
        # Pulihkan karakter HP
        enemy['hp']  = initial_enemy_hp
        player['hp']  = initial_player_hp

        return monster

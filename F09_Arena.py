from F00_RandomGenerator import *
from F08_Battle import *
from user_interface import *

def combat_arena(user_id, user_data, player, monster, item_inventory, player_level, stage):
    key = str(interval(1, len(monster)))
    lvl_monster = stage
    initial_enemy_hp = enemy['hp']
    enemy['atk_power'], enemy['def_power'], enemy['hp'] = upgrade_stat(enemy, str(lvl_monster))
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

    turn = 1
    potion_used = [False, False, False]

    while int(player['hp']) > 0 and int(enemy['hp']) > 0:
        print(f"============ TURN {turn} ({player['type']}) ============")
        pilih = menu("Attack", "Use Potion", "Quit")

        if pilih == '1':
            if player_attack(player, enemy, player_level):
                print(f"\nSelamat, Anda berhasil mengalahkan monster {enemy['type']} !!!\n")
                OC_reward = interval(10, 100)
                print(f"Total OC yang diperoleh: {OC_reward}\n")
                owca_coin = int(user_data['oc']) + OC_reward
                user_data['oc'] = str(owca_coin)
                return (True, item_inventory)

        elif pilih == '2':
                print("========POTION LIST===========") 

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
                                print("Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia")
                                print("menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
                            else:
                                print("Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi")
                                print("Pikachow dan gerakannya menjadi lebih cepat dan mematikan.\n")
                                potion_effects = efek_potion('strength', player)
                                player['atk_power'] = potion_effects[0]
                                sisa_potion1 -= 1
                                potion_used[0] = True # Potion 1 telah dipakai
                                break
                                
                        else:
                            print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!\n")
                            continue

                    elif perintah == '2':
                        if sisa_potion2 > 0:
                            if potion_used[1]:
                                print("Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia menolaknya")
                                print("seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
                            else: 
                                print("Setelah meminum ramuan ini, muncul sebuah energi pelindung di")
                                print("sekitar Pikachow yang membuatnya terlihat semakin tangguh dan sulit dilukai.\n")
                                potion_effects = efek_potion('resilience', player)
                                player['def_power'] = potion_effects[1]
                                sisa_potion2 -= 1
                                potion_used[1] = True # Potion 2 telah dipakai
                                break
                        
                        else:
                            print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!\n")
                            continue

                    elif perintah == '3':
                        if sisa_potion3 > 0:
                            if potion_used[2]:
                                print("Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia menolaknya")
                                print("seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
                            else:     
                                print("Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh Pikachow sembuh dengan cepat.")
                                print("Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.\n")
                                potion_effects = efek_potion('healing', player)
                                player['hp'] = potion_effects[2]
                                sisa_potion3 -= 1
                                potion_used[2] = True # Potion 3 telah dipakai
                                break
                        
                        else:
                            print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!\n")
                            continue

                    elif perintah == '4':
                        break

                    else:
                        print("Item tidak tersedia!!!\n")
            
                # Update quantity potion dalam dictionary 'item_inventory'
                item_user[0]['quantity'] = sisa_potion1
                item_user[1]['quantity'] = sisa_potion2
                item_user[2]['quantity'] = sisa_potion3
                item_inventory[user_id] = item_user

        elif pilih == '3':
            print("GAME OVER! Anda mengakhiri sesi latihan!")
            loading("Keluar...")
            return (False, item_inventory)

        else:
            print("Pilihan tidak tersedia!")

        print(f"============ TURN {turn} ({enemy['type']}) ============")
        if enemy_attack(enemy, player, lvl_monster):
            print(f"\nYahhh, Anda dikalahkan monster {enemy['type']}. Jangan menyerah, coba lagi !!!\n")
            return (False, item_inventory)

        turn += 1

    return (False, item_inventory)

def main_arena(user_id, user_data, monster, monster_inventory, item_inventory):
    starter("\n ======== SELAMAT DATANG DI ARENA!!! ==========")
    
    while True:  # Loop until a valid monster is selected
        display_user_monsters(user_id, monster_inventory, monster)
        pilih_monster = input(str(">> Pilih monster untuk bertarung: "))

        if pilih_monster.isdigit() and 0 < int(pilih_monster) <= len(monster_inventory[user_id]):
            player = monster[monster_inventory[user_id][int(pilih_monster) - 1]['monster_id']]
            player_level = monster_inventory[user_id][int(pilih_monster) - 1]['level']
            player['atk_power'], player['def_power'], player['hp'] = upgrade_stat(player, str(player_level))
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
            print("-----------------------------------------------------------")
            print(f"\nRAWRRR, Agent {user_data['username']} mengeluarkan monster {player['type']}!!!")
            print("Nama       :", player['type'])
            print("ATK power  :", player['atk_power'])
            print("DEF power  :", player['def_power'])
            print("HP         :", player['hp'])
            print("Level      :", player_level)

            total_reward = 0
            successful_stages = 0
            total_damage_given = 0
            total_damage_taken = 0

            for stage in range(1, 6):
                print(f"\n============= STAGE {stage} ===============")
                player_starting_hp = player['hp']

                stage_result, item_inventory = combat_arena(user_id, user_data, player, monster, item_inventory, player_level, stage)
                if stage_result:
                    total_reward += reward[str(stage)]
                    successful_stages += 1
                    total_damage_given += int(player['atk_power'])
                    total_damage_taken += int(monster[str(interval(1, len(monster)))]['atk_power'])
                    print(f"STAGE CLEARED!! Anda mendapatkan {reward[str(stage)]} OC pada sesi ini!")
                    if stage == 5:
                        print("Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
                    else:
                        print("Memulai stage berikutnya...")
                else:
                    total_damage_given += int(player['atk_power'])
                    total_damage_taken += int(monster[str(interval(1, len(monster)))]['atk_power'])
                    print(f"GAME OVER!! Sesi latihan berakhir pada stage {stage}.")
                    break

                # Pulihkan karakter HP
                player['hp'] = player_starting_hp

            print("\n======== STATS ARENA =========")
            print(f"Total hadiah    : {total_reward} OC")
            print(f"Jumlah stage    : {successful_stages}")
            print(f"Damage diberikan: {total_damage_given}")
            print(f"Damage diterima : {total_damage_taken}")

            owca_coin = int(user_data['oc']) + total_reward
            user_data['oc'] = str(owca_coin)
            
            return user_data, item_inventory, monster

        else:
            print("Pilihan tidak tersedia! Silakan pilih lagi.\n")

reward = {
    '1': 30,
    '2': 60,
    '3': 90,
    '4': 120,
    '5': 150}

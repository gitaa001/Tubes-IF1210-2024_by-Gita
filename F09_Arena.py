from F00_RandomGenerator import *
from F08_Battle import display_user_monsters

def battle_arena(player, enemy):
    player_health = int(player['hp'])
    enemy_health  = int(enemy['hp'])
    while player_health > 0 and enemy_health > 0:
        # Player menyerang
        enemy_health -= int(player['atk_power'])
        print(f"{player['type']} menyerang {enemy['type']}!")

        if enemy_health <= 0:
            print(f"\nSelamat, Anda berhasil mengalahkan monster {enemy['type']} !!!\n")
            return True  # Enemy kalah
        else:
            # Enemy menyerang
            player_health -= int(enemy['atk_power'])
            print(f"{enemy['type']} menyerang {player['type']}!")

    if player_health <= 0:
        print(f"Yahhh, Anda dikalahkan monster {enemy['type']}. Jangan menyerah, coba lagi !!!")
        return False  # Player kalah

def arena(user_id, user_data, monster, monster_inventory):
    print("Selamat datang di arena!!!")

    print("\n======MONSTER LIST======")
    # Menampilkan pilihan monster player sesuai kepemilikan di 'monster_inventory'
    display_user_monsters(user_id, monster_inventory, monster)

    while True:
        pilih_monster = input(str(">> Pilih monster untuk bertarung: "))
        player = monster[pilih_monster]
        player_level = monster_inventory[user_id][int(pilih_monster)]['level']
        if pilih_monster in monster:
            print("-----------------------------------------------------------")
            print(f"\nRAWRRR, Agent {user_data['username']} mengeluarkan monster {player['type']}!!!")
            print("Nama       :", player['type'])
            print("ATK power  :", player['atk_power'])
            print("DEF power  :", player['def_power'])
            print("HP         :", player['hp'])
            print("Level      :", player_level)

            total_reward       = 0
            successful_stages  = 0
            total_damage_given = 0
            total_damage_taken = 0

            for stage in range(1,6): #5 STAGE
                    print(f"\n======== STAGE {stage} ==========")

                    # Spesifikasi monster musuh
                    RNG_monster = interval(1, len(monster))
                    x = str(RNG_monster)
                    enemy = monster[x]
                    print(f"\nRAWRRR, Monster {enemy['type']} telah muncul !!!")

                    # Memulihkan HP player
                    player_starting_hp = player['hp']

                    if battle_arena(player, enemy):
                        # Player menang
                        total_reward += reward[str(stage)]
                        successful_stages  += 1
                        total_damage_given += int(player['atk_power'])
                        total_damage_taken += int(enemy['atk_power'])
                        print(f"STAGE CLEARED!! Anda mendapatkan {reward[str(stage)]} OC pada sesi ini!")
                        if stage == 5:
                            print("Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
                        else:
                            print("Memulai stage berikutnya...")

                    else:
                        # Player kalah
                        total_damage_given += int(player['atk_power'])
                        total_damage_taken += int(enemy['atk_power'])
                        print(f"GAME OVER!! Sesi latihan berakhir pada stage {stage}.")
                        break          
                    
                    # Memulihkan health player setelah setiap stage
                    player['hp'] = player_starting_hp

            print("\n======== STATS ARENA =========")
            print(f"Total hadiah    : {total_reward} OC")
            print(f"Jumlah stage    : {successful_stages}")
            print(f"Damage diberikan: {total_damage_given}")
            print(f"Damage diterima : {total_damage_taken}")

            break

        else:
            print("Pilihan tidak tersedia!")

        return total_reward
     
reward = {
        '1': 30, 
        '2': 60, 
        '3': 90, 
        '4': 120,
        '5': 150}




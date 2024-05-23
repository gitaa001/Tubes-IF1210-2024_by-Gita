from F04_Help import help_before_login

def login(user):
    islogin = False
    user_id = None
    user_data = None
    
    # Cek apakah pengguna sudah login sebelumnya
    if islogin:
        print("Login gagal!")
        print(f'Anda sudah log in dengan username {user_data['username']}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali.')
        return user_id, user_data

    while not islogin:
        print("\n========== LOGIN ==========")
        username = input("Username: ")
        password = input("Password: ")
        cekusername = False
        cekpassword = False

        for uid, data in user.items():
            if data['username'] == username:
                cekusername = True
                if data['password'] == password:
                    cekpassword = True
                    user_id = uid
                    user_data = data
                    break

        if cekusername:
            if cekpassword:
                print("Login Berhasil!")
                islogin = True  # Set islogin menjadi True setelah berhasil login
                break

            else:
                print("Password Salah!")
                        
        else:
            print("Username Tidak Terdaftar!")
            pilih = input("Belum punya akun? Silakan lakukan register (y/n): ")
            if pilih.lower() == 'y':
                help_before_login()
                while True:
                    pilih = input("\n>>> Masukkan pilihan: ").lower()
                    if pilih.lower() == 'register' or pilih.lower() == 'login':
                        break
                    else:
                        continue
            else:
                continue

    return user_id, user_data

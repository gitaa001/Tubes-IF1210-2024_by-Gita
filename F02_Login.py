islogin = False

def login(user):
    global islogin
    user_id = None
    user_data = None
    
    if islogin:
        print("Login gagal!")
        print(f'Anda sudah log in, silahkan lakukan "LOGOUT" sebelum melakukan login kembali.')
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
                islogin = True
                break

            else:
                print("Password Salah!")
                        
        else:
            print("Username Tidak Terdaftar!")

    return user_id, user_data

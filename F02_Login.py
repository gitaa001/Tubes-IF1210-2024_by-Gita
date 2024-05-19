from user_interface import starter

islogin = False

def login(user):
    global islogin
    user_id = None  # Variabel untuk menyimpan ID pengguna yang berhasil login
    user_data = None  # Variabel untuk menyimpan data pengguna yang berhasil login
    
    while not islogin:
        print("\n========== LOGIN ==========")
        username=input("Username: ")
        password=input("Password: ")
        cekusername=False
        cekpassword=False

        for uid, data in user.items():
            user_check = data
            if user_check['username'] == username:
                cekusername=True
                if user_check['password'] == password:
                    cekpassword= True
                    user_id = uid
                    user_data = data

                else:
                    next
            else:
                next
        
        if cekusername:
            if cekpassword:
                print("Login Berhasil!")
                islogin = True
                break
            else:
                print("Password Salah!")
                
        else:
            print("Username Tidak Terdaftar!")
    else:
        username = user['username']
        print("Login gagal!")
        print(f'Anda sudah log in dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali.')
    
    # print(user_id) # string
    # print(user_data) # dict of string
    return user_id, user_data



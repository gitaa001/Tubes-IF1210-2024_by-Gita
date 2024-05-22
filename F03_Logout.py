# Insisiasi login
islogin = False
original_user_data = None

#Fungsi logout
def logout(user_id, user_data):
    global islogin
    islogin = False
    user_id = None
    user_data = None
    print("Anda telah logout, Sayonara!\n")
    return user_id, user_data

# Fungsi untuk memproses logout
def logging_out(user_id, user_data):
    global original_user_data, islogin
    
    logged_in = user_id is not None

    if logged_in:
        user_id, user_data = logout(user_id, user_data)
        
    else:
        print("Logout Gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")

    # Kembalikan data pengguna ke kondisi semula setelah logout
    user_data = original_user_data
    islogin = False  # Setelah logout, pastikan islogin diatur kembali ke False

    return user_id, user_data

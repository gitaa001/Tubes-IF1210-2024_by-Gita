islogin = False  # Pastikan islogin diinisialisasi sebagai global
original_user_data = None  # Variabel global untuk menyimpan data user sebelum logout

def logout(user_id, user_data):
    global islogin, original_user_data
    
    # Simpan data pengguna sebelum mengatur ke None
    original_user_data = user_data
    
    islogin = False  
    user_id = None
    user_data = None

    print("Anda telah logout, Sayonara!")
    
    return user_id, user_data  

def logging_out(user_id, user_data):
    global original_user_data
    
    logged_in = user_id is not None

    if logged_in:
        user_id, user_data = logout(user_id, user_data)
    else:
        print("Logout Gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")

    # Kembalikan data pengguna ke kondisi semula setelah logout
    user_data = original_user_data
    
    return user_id, user_data

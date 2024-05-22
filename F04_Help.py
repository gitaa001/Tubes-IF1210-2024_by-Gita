from user_interface import *

# Fungsi untuk menampilkan bantuan sebelum login

def help_before_login():
    starter("\n===================== H E L P =============================")
    print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
    print("Login: Masuk ke dalam akun yang sudah terdaftar")
    print("Register: Membuat akun baru")
    print("-------------------------------------------------")
    print("Footnote: ")
    print("Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("Jangan lupa untuk memasukkan input yang valid")
    print("-------------------------------------------------")

# Fungsi untuk menampilkan bantuan setelah login sebagai Agent
def help_as_agent(user_data):
    starter("\n===================== H E L P =============================")
    print(f"Halo Agent {user_data['username']}! Kamu memanggil command HELP.")
    print("Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian.")
    print("Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
    print("Logout: KELUAR dari akun yang sedang digunakan")
    print("Menu: Mengakses MENU UTAMA dan melakukan berbagai aksi")
    print("-------------------------------------------------")
    print("Footnote: ")
    print("Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("Jangan lupa untuk memasukkan input yang valid")
    print("-------------------------------------------------")

# Fungsi untuk menampilkan bantuan setelah login sebagai Admin
def help_as_admin():
    starter("\n===================== H E L P =============================")
    print(f"Selamat datang, Admin.")
    print("Berikut adalah hal-hal yang dapat kamu lakukan:")
    print("Logout: Keluar dari akun yang sedang digunakan")
    print("Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
    print("Footnote: ")
    print("-------------------------------------------------")
    print("Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("Jangan lupa untuk memasukkan input yang valid")
    print("-------------------------------------------------")






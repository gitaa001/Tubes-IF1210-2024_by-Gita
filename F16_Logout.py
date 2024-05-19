import os

def save_file():
    # Implementasi fungsi penyimpanan file (F15)
    print("File telah disimpan.")

def main():
    while True:
        user_input = input(">>> Do you want to exit? (y/n)")
        if user_input.upper() == "y":
            save_confirmation = input("Apakah Anda ingin melakukan penyimpanan? (y/n) ")
            # if save_confirmation.lower() == "y":
            #     import F15_Save
            #     save_file()
            #     print("Sampai jumpa lagi!")
            #     break

            # elif save_confirmation.lower() == "n":
            #     os.system('cls')
            #     break

        #     else:
        #         break
        # else:
        #     # Proses input lainnya
        #     pass

# main()
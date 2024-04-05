from ipul import login
def main():
    # Membuat objek login
    password_benar = "password123"
    akun = login(password_benar)
    
    while True: 
        password = input("Masukkan kata sandi: ")   
        if akun.cek_pass(password):
            print("Lanjutkan eksekusi program.")
            break

if __name__ == "__main__":
    main()

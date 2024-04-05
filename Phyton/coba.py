import time
class login:
    def cek_kata_sandi():
        email_benar = "redistaizza@gmail.com"
        password_benar = "12345"
        kesempatan = 3

        while kesempatan > 0:
            email = input("Masukkan email : ")
            password = input("masukkan password : ")
            if email == email_benar and password == password_benar:
                print("akun benar. Akses diberikan!")
                return True
            else:
                kesempatan -= 1
                if kesempatan > 0:
                    print(f"Kata sandi salah. Anda memiliki {kesempatan} kesempatan lagi.")
                else:
                    print("Anda telah mencoba 3 kali. Tunggu 3 detik sebelum mencoba lagi.")
                    time.sleep(3)
                    pertanyaan = input("apakah anda ingin melanjutkan(y/n) = ")
                    if pertanyaan == "y":
                        kesempatan = 3
                    if pertanyaan =="n":
                        break
                    return False

    if not cek_kata_sandi():
        print("Program terkunci.")
    else:
        print("Lanjutkan eksekusi program.")
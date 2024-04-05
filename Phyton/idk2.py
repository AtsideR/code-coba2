import time

class Login:
    def __init__(self, password):
        self.password = password
        self.kesempatan = 3

    def cek_pass(self, password):
        while self.kesempatan > 0:
            if password == self.password:
                print("Kata sandi benar. Akses diberikan!")
                return True
            else:
                self.kesempatan -= 1
                if self.kesempatan > 0:
                    print(f"Kata sandi salah. Anda memiliki {self.kesempatan} kesempatan lagi.")
                else:
                    print("Anda telah mencoba 3 kali. Tunggu 3 detik sebelum mencoba lagi.")
                    time.sleep(3)
                    pertanyaan = input("Apakah anda ingin melanjutkan (y/n)? ")
                    if pertanyaan.lower() == "y":
                        self.kesempatan = 3
                    else:
                        break
        return False

def main():
    kata_sandi_benar = "password123"
    login_instance = Login(kata_sandi_benar)

    password_valid = False
    while not password_valid:
        password = input("Masukkan kata sandi: ")
        password_valid = login_instance.cek_pass(password)
        if password_valid:
            print("Lanjutkan eksekusi program.")
            break

if __name__ == "__main__":
    main()

import time
class Akun:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.gagal_login = 0
        self.terkunci = False

    def coba_login(self, username, password):
        if self.terkunci:
            print("Akun telah terkunci.")
            return False        
        if username == self.username and password == self.password:
            print("Login berhasil.")
            self.gagal_login = 0
            return True
        else:
            print("Login gagal.")
            self.gagal_login += 1
            if self.gagal_login >= 3:
                self.terkunci = True
                print("Akun telah terkunci karena terlalu banyak percobaan login gagal.")
                time.sleep(3)
                self.gagal_login == 0
            return False
    
    
def main():
    username_benar = "udin"
    password_benar = "12345"

    akun = Akun(username_benar, password_benar)

    for _ in range(3):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if akun.coba_login(username, password):
            break
        print()

if __name__ == "__main__":
    main()

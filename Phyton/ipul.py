import time

class login:    
    def __init__ (self, password):
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
                    pertanyaan = input("apakah anda ingin melanjutkan(y/n) = ")
                    if pertanyaan == "y":
                        self.kesempatan = 3
                    else: 
                        self.kesempatan = 0   
                        print("program terkunci")
                        break
                return False
            
            
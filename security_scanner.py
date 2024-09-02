import os
import time
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

# Kullanıcı işlemlerini takip etmek için bir liste
user_activity_log = []

def clear_screen():
    os.system('clear')

def print_menu():
    clear_screen()
    print(Fore.BLUE + """
   ____ ____      _    _____ _____ ___   ___  _     
  / ___|  _ \    / \  |  ___|_   _/ _ \ / _ \| |    
 | |  _| |_) |  / _ \ | |_    | || | | | | | | |    
 | |_| |  _ <  / ___ \|  _|   | || |_| | |_| | |___ 
  \____|_| \_\/_/   \_\_|     |_| \___/ \___/|_____|
                                                    
""")
    print(Fore.RED + """
   _____ ______ _____ _    _ _____  _____ _________     __   _____  _____          _   _ _   _ ______ _____  
  / ____|  ____/ ____| |  | |  __ \|_   _|__   __\ \   / /  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | (___ | |__ | |    | |  | | |__) | | |    | |   \ \_/ /  | (___ | |       /  \  |  \| |  \| | |__  | |__) |
  \___ \|  __|| |    | |  | |  _  /  | |    | |    \   /    \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
  ____) | |___| |____| |__| | | \ \ _| |_   | |     | |     ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_____/|______\_____|\____/|_|  \_\_____|  |_|     |_|    |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\
                                                                                                             
                                                                                                                                                                                             
                                                                                                                                          
""")
    print(Fore.YELLOW + "Developer: carbans2717")
    print(Fore.GREEN + "[01] Çıkış")
    print(Fore.GREEN + "[02] Güvenlik Açığı Taraması")
    print(Fore.GREEN + "[03] Admin Panel")

def check_security_vulnerabilities(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            headers = response.headers
            soup = BeautifulSoup(response.text, 'html.parser')

            # Basit güvenlik açığı kontrolü
            security_issue_detected = False
            
            if 'x-amz-server-side-encryption' not in headers:
                user_activity_log.append(f"Site {url} için güvenlik açığı: Sunucu tarafı şifreleme başlığı bulunmuyor.")
                security_issue_detected = True

            # Meta bilgileri kontrol et
            meta_tags = soup.find_all('meta')
            robots_meta = any(meta.get('name') == 'robots' and 'noindex' in meta.get('content', '') for meta in meta_tags)
            if robots_meta:
                user_activity_log.append(f"Site {url} için güvenlik açığı: robots meta etiketi noindex içeriyor.")
                security_issue_detected = True
            
            if not security_issue_detected:
                user_activity_log.append(f"Site {url} için güvenlik açığı bulunmadı.")
        else:
            user_activity_log.append(f"Site {url} erişilemedi. HTTP durum kodu: {response.status_code}")

    except Exception as e:
        user_activity_log.append(f"Hata: {e}")
        user_activity_log.append("Güvenlik açığı durumu bilinmiyor.")

def admin_panel():
    clear_screen()
    print(Fore.RED + "Admin Şifresi:")
    password = input()
    if password == "graftooladminkey":
        clear_screen()
        print(Fore.GREEN + "Admin terminaline hoş geldiniz!")
        print(Fore.GREEN + "Kullanıcı aktiviteleri:")
        for activity in user_activity_log:
            print(Fore.GREEN + activity)
        
        input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
    else:
        print(Fore.RED + "Yanlış şifre. Geri dönülüyor...")
        time.sleep(1)

def main():
    while True:
        print_menu()
        choice = input(Fore.GREEN + "Seçiminizi yapın (1, 2 veya 3): ")

        if choice == '1':
            clear_screen()
            print(Fore.GREEN + "Çıkış yapılıyor...")
            time.sleep(1)
            break
        elif choice == '2':
            clear_screen()
            url = input(Fore.GREEN + "Site (örn. http://example.com veya https://example.com): ")
            check_security_vulnerabilities(url)
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '3':
            admin_panel()
        else:
            clear_screen()
            print(Fore.RED + "Geçersiz seçim. Lütfen tekrar deneyin.")
            time.sleep(1)

if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup

def check_security_vulnerabilities(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print("Tarama tamamlandı. Site erişilebilir.")
            headers = response.headers
            soup = BeautifulSoup(response.text, 'html.parser')

            # Basit güvenlik açığı kontrolü
            security_issue_detected = False
            
            if 'x-amz-server-side-encryption' not in headers:
                print("Güvenlik açığı var: Sunucu tarafı şifreleme başlığı bulunmuyor.")
                security_issue_detected = True

            # Meta bilgileri kontrol et
            meta_tags = soup.find_all('meta')
            robots_meta = any(meta.get('name') == 'robots' and 'noindex' in meta.get('content', '') for meta in meta_tags)
            if robots_meta:
                print("Güvenlik açığı var: robots meta etiketi noindex içeriyor.")
                security_issue_detected = True
            
            if not security_issue_detected:
                print("Güvenlik açığı yok.")
        else:
            print(f"Siteye erişim sağlanamadı. HTTP durum kodu: {response.status_code}")

    except Exception as e:
        print(f"Hata: {e}")
        print("Güvenlik açığı durumu bilinmiyor.")

def main():
    print("1. Güvenlik açığı taraması")
    choice = input("Seçiminizi yapın (1): ")
    if choice == '1':
        url = input("Site (örn. http://example.com veya https://example.com): ")
        check_security_vulnerabilities(url)
    else:
        print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()

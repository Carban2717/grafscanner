import requests
from bs4 import BeautifulSoup

def check_security_vulnerabilities(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Tarama tamamlandı. Site erişilebilir.")
            # Basit bir güvenlik taraması: HTTP başlıklarını kontrol etme
            headers = response.headers
            print("\nHTTP Başlıkları:")
            for header, value in headers.items():
                print(f"{header}: {value}")
            # Basit bir içerik taraması: Başlıkları ve meta bilgileri kontrol etme
            soup = BeautifulSoup(response.text, 'html.parser')
            print("\nBaşlıklar ve Meta Bilgiler:")
            print(f"Başlık: {soup.title.string if soup.title else 'Bulunamadı'}")
            for meta in soup.find_all('meta'):
                print(f"Meta: {meta.get('name', 'İsimsiz')} - {meta.get('content', 'İçerik bulunamadı')}")
        else:
            print(f"Siteye erişim sağlanamadı. HTTP durum kodu: {response.status_code}")
    except Exception as e:
        print(f"Hata: {e}")

def main():
    print("1. Güvenlik açığı taraması")
    choice = input("Seçiminizi yapın (1): ")
    if choice == '1':
        url = input("Site: ")
        if url.startswith("http://") or url.startswith("https://"):
            check_security_vulnerabilities(url)
        else:
            print("Geçersiz URL. Lütfen 'http://' veya 'https://' ile başlayın.")
    else:
        print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()

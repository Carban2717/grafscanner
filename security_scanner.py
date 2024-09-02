import requests
from bs4 import BeautifulSoup

def check_security_vulnerabilities(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Tarama tamamlandı. Site erişilebilir.")
            headers = response.headers
            print("\nHTTP Başlıkları:")
            for header, value in headers.items():
                print(f"{header}: {value}")
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
        url = input("Site (örn. http://example.com veya https://example.com): ")
        check_security_vulnerabilities(url)
    else:
        print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()

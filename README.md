# Test Otomasyon Portföyü

Python, pytest ve Playwright ile yazdığım test otomasyon örnekleri.

## İçerik

- `hesap_makinesi.py` ve `test_hesap_makinesi.py`: unit test örnekleri (pozitif, negatif ve hata durumu testleri)
- `test_login.py`: giriş formu için web otomasyon testi
- `test_saucedemo.py`: e-ticaret sitesinde ürün sepete ekleme ve yanlış şifre senaryoları

## Kurulum

pip3 install pytest pytest-playwright
python3 -m playwright install

## Testleri çalıştırma

python3 -m pytest

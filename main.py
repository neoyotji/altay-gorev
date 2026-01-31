import os
import sys
from config import kurallari_getir
from analyzer import satir_incele, dosyayi_izle, tespit_edilenler
from csv_report import rapor_olustur



def ana_menu():
    kural_listesi = kurallari_getir()
    
    while True:
        print("\n####### ALTAY LOG İZLEME GÖREVİ #######")
        print("1. Sistem loglarını tara")
        print("2. Realtime TailMode")
        print("3. Rapor Oluştur")
        print("4. Çıkış")
        
        secim = input(":")

        if secim == "1":
            print("\nSistem logları taranıyor.")
            otomatik_sistem_taramasi(kural_listesi)
            
            if tespit_edilenler:
                print("Tespitler bulundu, rapor dosyası oluşturuldu. 3. seçeneği seçiniz.")
                rapor_olustur(tespit_edilenler)
            else:
                print("[i] Herhangi bir tehdit tespit edilemediği için rapor oluşturulmadı.")

        elif secim == "2":
            yol = input("İzlenecek dosya yolu : ")
            if os.path.exists(yol):
                try:
                    print(f"Dosya izleniyor, durdurma yapabilirsiniz (ctrl+c)")
                    dosyayi_izle(yol, kural_listesi)
                except KeyboardInterrupt:
                    print("Kontrol durdu")
            else:
                print("Böyle bir dosya bulunamadı")

        elif secim == "3":
            rapor_olustur(tespit_edilenler)

        elif secim == "4":
            print("Program kapanıyor")
            break
        else:
            print("Seçim yapınız")


def otomatik_sistem_taramasi(kurallar):

    log_listesi = [
        "/var/log/auth.log",
        "/var/log/syslog",
        "/var/log/nginx/access.log",
        "/var/log/ufw.log"
    ]
    
    print("Sistem loglarını tara")

    for yol in log_listesi:
        if os.path.exists(yol):
            try:
                with open(yol, 'r', encoding='utf-8', errors='ignore') as f:
                    for satir in f:
                        satir_incele(satir, kurallar)
            except Exception as e:
                print(f"{yol} okunurken hata oluştu: {e}")
        else:
            print(f"{yol} bulunamadı")
            
    print("\nTarama tamamlandı. ")            

if __name__ == "__main__":
    ana_menu()

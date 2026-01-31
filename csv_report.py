import csv

def rapor_olustur(olay_listesi):
    if not olay_listesi:
        print("\n Tespit edilen bir olay yok.")
        return

    dosya_adi = "log_raporu.csv"
    basliklar = ["zaman", "kural", "mesaj"]

    try:
        with open(dosya_adi, mode='w', newline='', encoding='utf-8') as f:
            yazici = csv.DictWriter(f, fieldnames=basliklar)
            yazici.writeheader()
            yazici.writerows(olay_listesi)
        print(f"\n Rapor oluşturuldu: {dosya_adi}")
    except Exception as e:
        print(f"\n Rapor oluşturulurken hata oluştu: {e}")
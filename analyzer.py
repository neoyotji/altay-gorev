import time
import base64
import os
import re

olay_hafizasi = {} 

def log_decode(satir):
    try:
        if len(satir) > 20 and "=" in satir:
            decoded = base64.b64decode(satir).decode('utf-8')
            return decoded
    except:
        pass
    return satir

tespit_edilenler = []

def satir_incele(satir, kurallar):
    temiz_satir = log_decode(satir)
    simdi = time.time()
    bulundu_mu = False

    for kural in kurallar:
        anahtar = kural.get('anahtar_kelime') or kural.get('pattern')
        
        if anahtar in temiz_satir:
            kural_id = kural['id']
            if kural_id not in olay_hafizasi:
                olay_hafizasi[kural_id] = []
            
            olay_hafizasi[kural_id].append(simdi)
            pencere = kural.get('pencere_sn') or kural.get('time_window', 0)
            gecerli_olaylar = [t for t in olay_hafizasi[kural_id] if t > simdi - pencere]
            olay_hafizasi[kural_id] = gecerli_olaylar
            
            esik = kural.get('esik_degeri') or kural.get('threshold', 1)
            if len(gecerli_olaylar) >= esik:
                olay = {
                    "zaman": time.strftime('%Y-%m-%d %H:%M:%S'),
                    "kural": kural.get('isim') or kural.get('name'),
                    "mesaj": temiz_satir.strip()
                }
                if olay not in tespit_edilenler:
                    tespit_edilenler.append(olay)
                
                print(f"{olay['kural']} tespit edild")
                bulundu_mu = True
    return bulundu_mu

def dosyayi_izle(dosya_yolu, kurallar):
    with open(dosya_yolu, 'r') as f:
        f.seek(0, 2)
        while True:
            satir = f.readline()
            if not satir:
                time.sleep(1)
                continue
            satir_incele(satir, kurallar)

def toplu_analiz_yap(kurallar):
    log_dosyalari = [
        "/var/log/auth.log",
        "/var/log/syslog",
        "/var/log/nginx/access.log",
        "/var/log/ufw.log"
    ]
    
    ozet_verisi = {}

    print("\nToplu Analiz Başlatıldı")
    for dosya_yolu in log_dosyalari:
        if os.path.exists(dosya_yolu):
            bulunan_tehdit_sayisi = 0
            
            with open(dosya_yolu, 'r', encoding='utf-8', errors='ignore') as f:
                for satir in f:
                    if satir_incele(satir, kurallar): 
                        bulunan_tehdit_sayisi += 1
            
            ozet_verisi[dosya_yolu] = bulunan_tehdit_sayisi
        else:
            ozet_verisi[dosya_yolu] = "Dosya Bulunamadı"

    print("ANALİZ RAPORU")
    for dosya, sonuc in ozet_verisi.items():
        print(f"{dosya.ljust(25)} : {sonuc} Olay Tespit Edildi")
    print("Analiz Tamamlandı\n")
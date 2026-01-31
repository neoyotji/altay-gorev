Docker konteynerini çalıştırırken host makinedeki log dizinini bağlamanız gerekir: docker run -it -v /var/log:/var/log log_araci

docker run -it -v /var/log:/logs altay_log_gorev

Çalışma mantığı ve işleyişi

Uygulama sistem üzerinde otomatik olarak girdiğim kullanıcı dosyalarını tarar ve csv dosyası olarak kaydeder.

Taranan dosyalarda hatalı login denemesi, ssh brute force, yetki yükseltme kulanımı ve UFW block bilgileri kontrol edilir.

Kontrol sonunda bulunan tehdit ve girişimler csv dosyasına özet olarak çıkartılır.

Uygulama dosya yapısından ötürü GNU/Linux dağıtımlarında çalışır (windows eğik çizgisi ve user bilgisinden 
dolayı çalışmz)

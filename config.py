import yaml

def kurallari_getir(dosya_yolu="rules/rules.yaml"):
    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            veri = yaml.safe_load(f)
            return veri['kurallar']
    except Exception as e:
        print(f"Kurallar yüklenirken hata: {e}")
        return []
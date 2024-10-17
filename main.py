import pandas as pd
import qrcode

# Excel dosyasını okuma
excel_file = 'veriler.xlsx'  # Excel dosya yolu
sheet_name = 'Sayfa1'  # Çalışma sayfası adı
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# ID sütununu seçme (örneğin ID sütunun adı 'id' ise)
id_column = df['id']

# Her ID için QR kodu oluşturma
for id_value in id_column:
    # QR kodu oluşturma
    qr = qrcode.QRCode(
        version=1,  # QR kod versiyonu, büyüklük ve içerik miktarına göre değişir
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
        box_size=10,  # QR kodunun boyutunu ayarlar
        border=4  # Kenarlık boyutu
    )
    
    qr.add_data(str(id_value))  # QR koduna ID'yi ekleme
    qr.make(fit=True)  # Otomatik boyutlandırma

    # QR kodu görselini oluşturma
    img = qr.make_image(fill='black', back_color='white')

    # QR kodunu kaydetme
    img.save(f'qr_codes/qr_{id_value}.png')

print("QR kodları başarıyla oluşturuldu.")

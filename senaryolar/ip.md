Müşteri, ağdaki birden fazla cihazın aynı IP adresini kullanması nedeniyle bağlantı hataları veya erişim sorunları yaşıyor. Örnek: “Bilgisayarım ‘IP adresi çakışması var’ diye uyarı veriyor ve ağa bağlanamıyor.”

# Olası Nedenler  
- DHCP sunucusunun hatalı IP dağıtımı (aynı IP’yi birden çok cihaza ataması)  
- Statik IP ataması yapılan cihazla DHCP’den atanmış IP’nin çakışması  
- DHCP kira süresinin (lease) yenilenememesi  
- Ağ cihazlarında (switch, router) yazılım/firmware uyumsuzluğu  
- Ağ topolojisi değişikliği sonrası IP havuzunun güncellenmemesi  
- VPN veya sanal ağ adaptörü IP adreslerini sistemiyle çakışması  
- Eski veya arızalı cihazların DHCP tablolarını temizlememesi  
- Manuel IP rezervasyonlarının yanlış yapılandırılması  

# Gerekli Bilgi ve Parametreler  
- DHCP sunucusunun IP havuzu aralığı ve mevcut atama tablosu  
- Sorun yaşayan cihazın mevcut IP adresi ve MAC adresi  
- Diğer ağ cihazlarının (bilgisayar, yazıcı, IoT) IP/MAC listesi  
- DHCP kira süresi ayarları ve son yenilenme zamanı  
- Statik IP tanımlı cihazların listesi ve yapılandırma detayları  
- Ağ üzerindeki DHCP relay veya ek sunucu varlığı  
- Router/switch modeli, firmware sürümü ve DHCP yapılandırması  
- VPN/virtual adapter ayarları ve atanan IP blokları  

# Hedef Cevap / Çözüm Adımları  
1. PC veya cihazda `ipconfig /all` (ya da benzeri) ile mevcut IP/MAC bilgisini tespit etme  
2. DHCP sunucu atama tablosunda aynı IP’yi kullanan diğer cihazı belirleme  
3. Statik IP tanımlı cihaz varsa bu adresi DHCP havuzunun dışına taşıma  
4. DHCP kiralama işlemini `release` ve `renew` ile yenileyerek farklı IP atama  
5. Gerekirse DHCP havuz aralığını güncelleyerek çakışma riskini minimize etme  
6. Router/switch cihazlarında DHCP yapılandırmasını kontrol edip firmware güncelleme  
7. VPN veya sanal adaptörlerin IP atama bloklarını ayrı subnetlere ayırma  
8. Ağ topolojisindeki IP dağıtım politikasını gözden geçirerek statik ve dinamik IP ayrımını standartlaştırma  

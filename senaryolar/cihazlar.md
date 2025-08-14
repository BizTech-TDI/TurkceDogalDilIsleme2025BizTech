Müşteri, belirli cihazların ağa bağlanamadığını veya oturum açamadığını bildiriyor. Örnek: “Dizüstü bilgisayarım ve tabletim Wi-Fi ağına bağlanamıyor, telefonum sorunsuz çalışıyor.”

# Olası Nedenler  
- Yanlış Wi-Fi şifre girişi veya şifre değişikliği  
- MAC adresi filtrelemesi veya kara liste ayarı  
- DHCP havuzunun dolması; yeni cihaz için IP atanamaması  
- Cihazdaki ağ adaptörü sürücü veya donanım sorunları  
- Cihazla erişim noktası arasındaki sinyal zayıflığı veya parazit  
- Misafir ağı ile ana ağ karışıklığı; cihazın yanlış SSID’ye yönlendirilmesi  
- Ağ güvenlik protokolü (WPA2/WPA3) uyumsuzluğu  
- Router üzerinde eşzamanlı bağlantı sayısı limiti  
- DHCP rezervasyon ayarlarında eksik kayıt  
- Cihazdaki statik IP ayarlarının hatalı yapılandırılması  

# Gerekli Bilgi ve Parametreler  
- Hangi cihaz türlerinin etkileniyor olduğu (PC, tablet, IoT cihazı vb.)  
- Kullanılan SSID ve şifreler ile erişim noktası yapılandırması  
- Router üzerinde etkin olan güvenlik protokolleri ve MAC filtreleme ayarları  
- IP dağıtım yöntemi (DHCP mi, statik IP mi?) ve mevcut IP havuzunun durumu  
- Cihazların ağ adaptörü sürüm ve sürücü bilgileri  
- Aynı anda bağlı cihaz sayısı ve eşzamanlı bağlantı limiti  
- Cihazın aldığı sinyal gücü ve parazit ölçümleri  
- Misafir ağı varsa misafir/ana ağ ayrımı bilgisi  
- DHCP rezervasyon listesi ve IP atanma geçmişi  

# Hedef Cevap / Çözüm Adımları  
1. Cihazda kayıtlı Wi-Fi ağını silip şifreyi yeniden girme  
2. Router’da MAC filtreleme ve kara liste ayarlarını kontrol ederek ilgili MAC adresini izinli listeye ekleme  
3. DHCP havuzunda boş IP olup olmadığını kontrol etme; gerekirse havuzu genişletme  
4. Cihaz ağ adaptörü sürücülerini güncelleme veya yeniden yükleme  
5. Cihaz ile erişim noktası arasındaki sinyal gücünü ölçme, gerekirse konumu değiştirme veya menzil genişletici ekleme  
6. Ağ güvenlik protokolü uyumluluğunu doğrulama (WPA2 vs. WPA3)  
7. Eşzamanlı bağlantı limiti ve misafir ağı yapılandırmasını gözden geçirme  
8. Statik IP kullanılıyorsa ayarların doğruluğunu kontrol etme ve DHCP rezervasyonu gerekiyorsa yapılandırma  

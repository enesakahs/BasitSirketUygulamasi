# Basit Sirket Maas Otomasyonu

Bu kodlar, bir şirketin çalışanlarını ve maaşlarını yönetmek için kullanılan bir otomasyon programını tanıtmaktadır. Program, Sirket adında bir sınıf içinde yer alan metodlar kullanılarak çalışmaktadır.

**Programın genel işleyişi aşağıdaki gibidir:**

Sirket sınıfı, ad adında bir şirket adı ve calisma adında bir boolean değer ile başlatılır. calisma değeri True olduğu sürece program çalışmaya devam eder.

Menu metodunda kullanıcıya bir menü sunulur ve seçim yapması istenir. Seçim, secim değişkenine kaydedilir ve döndürülür.

program metodunda Menu metodundan dönen seçime göre ilgili işlem yapılır. Seçime göre CalisanEkle, CalisanSil, VerilecekMaasGoster veya MaaslariVer metodları çağrılır.

CalisanEkle metodunda kullanıcıdan çalışan bilgileri alınır, bir ID atanır ve bu bilgiler calisanlar.txt adlı bir dosyaya yazılır.

CalisanSil metodunda calisanlar.txt adlı dosya okunarak mevcut çalışanlar listelenir ve kullanıcıdan bir çalışan numarası seçilmesi istenir. Seçilen çalışanın bilgileri listeden çıkarılır ve dosya güncellenir.

VerilecekMaasGoster metodunda calisanlar.txt adlı dosya okunarak çalışanların maaşları toplanır ve aylık veya yıllık olarak ekrana yazdırılır.

MaaslariVer metodunda calisanlar.txt adlı dosya okunarak çalışanların maaşları toplanır ve toplam maaş bütçeden düşülerek butce.txt adlı dosya güncellenir.

Son olarak, bir Sirket nesnesi oluşturulur ve calisma değeri True olduğu sürece program metodu sürekli olarak çağrılır, böylece kullanıcı sürekli olarak menüden seçim yapabilir ve program çalışmaya devam eder.

from django.contrib.auth.models import User
from djongo import models

# Create your models here.
from boards.models.models import IQBoard
from cards.models.managers import IQCardManager


class IQCardDurumlari(models.Model):
    durum = models.TextField(max_length=50, unique=True)

    def __str__(self):
        return self.durum


class IQCards(models.Model):
    """
    İş
kayıtlarının sahip olması gereken nitelikler; başlık, içerik, tanımlanmışsa planlanan başlangıç ve bitiş
tarihi, oluşturulma tarihi, tamamlanma tarihi, durum (yönetim paneli yapacaksanız dinamik,
yapmayacaksanız, alındı, başladı, kontrolde, tamamlandı şeklinde dört durum yeterli), eğer kullanıcı
yönetimi yapacaksanız sahip ve atanmış kişidir.
    """

    metin = models.TextField(name='metin', max_length=150, help_text='Kartı tanımlayın')
    icerik = models.TextField(name='icerik', max_length=250, help_text='Kart icerigi')
    pl_baslangic = models.DateTimeField(help_text='Planlanan başlama tarihi')
    pl_bitis = models.DateTimeField(help_text='Planlanan bitiş tarihi')
    durum = models.ForeignKey(IQCardDurumlari, on_delete=models.CASCADE)

    sahip = models.ForeignKey(User, on_delete=models.CASCADE, name='sahip', related_name='sahip')
    atanmis = models.ForeignKey(User, on_delete=models.CASCADE, name='atanmis', related_name='atanmis')

    board = models.ForeignKey(IQBoard, on_delete=models.CASCADE)

    objects = IQCardManager()

    """
    Eğer bir iş kaydının başlangıç tarihi geçmesine rağmen durumu başladı diye belirlenmediyse
kullanıcıya e-posta gitmesi gerekmekte. Aynı şekilde bitiş tarihi geçmesine rağmen durumu
tamamlandı diye belirlenmediyse kullanıcıya eposta gitmesi gerekmekte.
    """

    def __str__(self):
        return f"{self.board} - {self.durum}"
        # return f"{self.durum}"

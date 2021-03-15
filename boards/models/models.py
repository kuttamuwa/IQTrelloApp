from djongo import models

# Create your models here.
from boards.models.managers import IQBoardManager


class IQBoardDurum(models.Model):
    durum = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.durum


class IQBoard(models.Model):
    """
    * Aynı anda birden fazla aktif proje mevcut olabilir (trello'daki board'lar gibi düşünebilirsiniz). Projelerin
sahip olması gereken nitelikler; isim, durum (aktif, arşivlenmiş) oluşturulma tarihi, ve eğer kullanıcı
yönetimi yapacaksanız sahip ve görmeye yetkili kişilerdir.
    """

    isim = models.CharField(max_length=60)
    durum = models.ForeignKey(IQBoardDurum, on_delete=models.CASCADE)
    olusturulma_tarihi = models.DateTimeField(help_text='Opsiyonel', auto_now_add=True)

    objects = IQBoardManager()

    def __str__(self):
        return f"Board ismi : {self.isim} - durum : {self.durum}"

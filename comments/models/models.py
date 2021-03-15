from django.contrib.auth.models import User
from djongo import models

from cards.models.models import IQCards


class IQComments(models.Model):
    """
    İş kayıtlarının altında birden fazla yorum mevcut olabilir (trello'daki card'ların altındaki yorumlar gibi
düşünebilirsiniz). Yorumların sahip olması gereken nitelikler, içerik, tarih ve eğer kullanıcı yönetimi
yapacaksanız gönderendir.
    """

    icerik = models.TextField(max_length=500, help_text='Yorum giriniz')
    tarih = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(IQCards, on_delete=models.CASCADE)
    gonderen = models.ForeignKey(User, on_delete=models.PROTECT)
    objects = models.DjongoManager()

    def __str__(self):
        # return f"{self.tarih} - {self.gonderen}"
        return f"{self.card} - {self.icerik} : {self.tarih}"

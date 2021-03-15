from datetime import datetime

from django.db import models
from django.utils import timezone

from util.tools import YagGmailMailSender


class IQCardManager(models.Manager):
    def check_pl_tarihleri(self, *args, **kwargs):
        pl_baslangic = kwargs['pl_baslangic']
        durum = kwargs['durum']
        pl_bitis = kwargs['pl_bitis']
        user = kwargs['sahip']

        to = user.email
        content = None
        subject = None

        if pl_baslangic <= timezone.now() and durum != 'Başladı':
            content = 'Başlangıç tarihi geçmesine rağmen durumu başladı diye verilmemiş !'
            subject = "Tarih uyuşmazlığı"

        if pl_bitis <= timezone.now() and durum != 'Tamamlandı':
            content = 'Bitiş tarihi geçmesine rağmen durumu tamamlandı diye verilmemiş !'
            subject = "Tarih uyuşmazlığı"

        self.send_mail(to=to, content=content, subject=subject)

    def create(self, *args, **kwargs):
        """
        Eğer bir iş kaydının başlangıç tarihi geçmesine rağmen durumu başladı diye belirlenmediyse
kullanıcıya e-posta gitmesi gerekmekte. Aynı şekilde bitiş tarihi geçmesine rağmen durumu
tamamlandı diye belirlenmediyse kullanıcıya eposta gitmesi gerekmekte.
        :param args:
        :param kwargs:
        :return:
        """
        self.check_pl_tarihleri(*args, **kwargs)

        return super(IQCardManager, self).create(*args, **kwargs)

    def send_mail(self, *args, **kwargs):
        """
        Mail server'a istek atilir veya sql server filansa komut calistirilir ama bizde mongo vs. vs. vs.
         try:
            requests.post('')

        except Exception as err:
            # logging
            pass
        :return:
        """
        if kwargs.get('content') is not None:
            return YagGmailMailSender.send_mail(*args, **kwargs)

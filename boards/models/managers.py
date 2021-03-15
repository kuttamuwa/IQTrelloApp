from datetime import datetime

from django.db import models


class IQBoardManager(models.Manager):
    def create(self, *args, **kwargs):
        """
        Board kayit edilirken bir seyler yapilacak mi?
        :param args:
        :param kwargs:
        :return:
        """
        if kwargs['olusturulma_tarihi'] is None:
            kwargs['olusturulma_tarihi'] = datetime.now()

        return super(IQBoardManager, self).create(*args, **kwargs)

    def send_mail(self):
        """
        Mail server'a istek atilir veya sql server filansa komut calistirilir ama bizde mongo vs. vs. vs.
         try:
            requests.post('')

        except Exception as err:
            # logging
            pass
        :return:
        """
        pass

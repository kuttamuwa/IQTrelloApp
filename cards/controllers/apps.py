from django.apps import AppConfig

from IQTrelloLatest.settings import DEBUG


class CardsConfig(AppConfig):
    name = 'cards'

    def ready(self):
        """
        Uygulama acilirken durum sutunlari doldurulsun
        :return:
        """
        # pass
        if not DEBUG:
            self.add_sabit_durumlar()

    def add_sabit_durumlar(self):
        from cards.controllers.hookers import DurumEkleHooker
        DurumEkleHooker().add_sabit_durumlar()

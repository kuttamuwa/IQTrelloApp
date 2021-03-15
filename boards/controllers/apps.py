from django.apps import AppConfig

from IQTrelloLatest.settings import DEBUG


class BoardsConfig(AppConfig):
    name = 'boards'

    def add_sabit_durumlar(self):
        from boards.controllers.hookers import BoardDurumEkleHooker
        BoardDurumEkleHooker.add_sabit_durumlar()

    def ready(self):
        if not DEBUG:
            print("board sabit durumlari ekleniyor..")
            self.add_sabit_durumlar()

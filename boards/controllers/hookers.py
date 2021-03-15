from boards.models.models import IQBoardDurum


class BoardDurumEkleHooker:
    @staticmethod
    def add_sabit_durumlar():
        IQBoardDurum.objects.get_or_create(durum='AKTIF')
        IQBoardDurum.objects.get_or_create(durum='ARSIVLENMIS')
        print("Board sabit durumları eklendi")
from cards.models.models import IQCardDurumlari


class DurumEkleHooker:
    @staticmethod
    def add_sabit_durumlar():
        IQCardDurumlari.objects.get_or_create(durum='Başladı')
        IQCardDurumlari.objects.get_or_create(durum='Alındı')
        IQCardDurumlari.objects.get_or_create(durum='Tamamlandı')
        IQCardDurumlari.objects.get_or_create(durum='Kontrolde')
        print("Kart sabit durumlari eklendi")
        # from cards.tests.tests import TestDurumlariEkle
        # TestDurumlariEkle().test_add_sabit_durumlar()

from django.test import TestCase

# Create your tests here.
from cards.models.models import IQCardDurumlari


class TestDurumlariEkle(TestCase):
    def test_add_sabit_durumlar(self):
        IQCardDurumlari.objects.get_or_create(durum='Başladı')
        IQCardDurumlari.objects.get_or_create(durum='Alındı')
        IQCardDurumlari.objects.get_or_create(durum='Tamamlandı')
        IQCardDurumlari.objects.get_or_create(durum='Kontrolde')

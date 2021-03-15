from django.contrib import admin

# Register your models here.
from cards.models.models import IQCards, IQCardDurumlari

admin.site.register(IQCards)
admin.site.register(IQCardDurumlari)


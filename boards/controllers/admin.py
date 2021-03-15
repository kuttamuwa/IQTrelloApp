from django.contrib import admin
from boards.models.models import IQBoard, IQBoardDurum

# Register your models here.
admin.site.register(IQBoard)
admin.site.register(IQBoardDurum)

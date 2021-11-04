from django.contrib import admin
from .models import JazzCategory, genre, region, character, era

# Register your models here.
admin.site.register(JazzCategory)
admin.site.register(genre)
admin.site.register(region)
admin.site.register(character)
admin.site.register(era)

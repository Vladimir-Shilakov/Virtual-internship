from django.contrib import admin
from .models import User, Coords, Mountain, Images, Level


admin.site.register(User)
admin.site.register(Coords)
admin.site.register(Level)
admin.site.register(Mountain)
admin.site.register(Images)

from django.contrib import admin

# Register your models here.
from .models import Company
from .models import Restaurant
from .models import Provider
from .models import Ingredient
from  .models import Receta
from .models import Steps

admin.site.register(Company)
admin.site.register(Restaurant)
admin.site.register(Provider)
admin.site.register(Ingredient)
admin.site.register(Receta)
admin.site.register(Steps)


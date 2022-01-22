from django import forms
from .models import Company
from .models import Restaurant
from .models import Provider
from .models import Ingredient
from .models import Receta
from .models import Steps


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'address',
            'city',
            'state',
            'contacto',
            'notes',
            'email',
            'url_corp',
            'feeds'
        ]


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            'name',
            'description',
            'address',
            'city',
            'state',
            'zipcode',
            'contacto',
            'notes',
            'email',
            'url_corp',
            'feeds',
            'TINid'

        ]



class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'address',
            'city',
            'state',
            'contacto',
            'notes',
            'email',
            'url_corp',
            'feeds',
            'company',
            'providers',
            'chefs'
        ]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'provider',
            'name',
            'description',
            'presentation',
            'type',
            'price',
            'qty',
            'merma'

        ]

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = [
            'chef',
            'restaurant',
            'name',
            'description',
            'portions',
            'items',
            'mpcost',
            'prepacost',
            'portioncost',
            'mpestablish',
            'errormargin',
            'realratemp',
            'saleprice',
            'menuprice',
            'realsaleprice',
            'taxportion'

        ]



class StepsForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = [
            'preparacion',
            'merma',
            'qty'

        ]

from typing import Tuple
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
import pgtrigger

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

User = get_user_model()

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_('name'), max_length=250)
    description = models.CharField(_('description'), max_length=250, blank=True)
    address = models.CharField(_('address'), max_length=100, blank=True)
    city = models.CharField(_('city'),max_length=100, blank=True)
    state = models.CharField(_('state'),max_length=100, blank=True)
    zipCode = models.CharField(_('zipCode'),max_length=100, blank=True)
    contacto = models.CharField(_('contacto'),max_length=100, blank=True)
    notes = models.CharField(_('notes'),max_length=250, blank=True)
    email = models.EmailField(_('email'),max_length=70,blank=True)
    phone = models.CharField(_('phone'),max_length=250, blank=True)
    url_corp = models.CharField(_('url'),max_length=250, blank=True)
    feeds = models.CharField(_('feeds'),max_length=250, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Company:detail', kwargs={
            'id':self.id
        })


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_('name'),max_length=250)
    description = models.CharField(_('description'),max_length=250, blank=True)
    address = models.CharField(_('address'),max_length=100, blank=True)
    city = models.CharField(_('city'),max_length=100, blank=True)
    state = models.CharField(_('state'),max_length=100, blank=True)
    zipcode = models.CharField(_('zipcode'),max_length=100, blank=True)
    contacto = models.CharField(_('contacto'),max_length=100, blank=True)
    notes = models.CharField(_('notes'),max_length=250, blank=True)
    email= models.EmailField(max_length=70,blank=True,unique=True)
    phone = models.CharField(_('phone'),max_length=250, blank=True)
    url_corp = models.CharField(_('url'),max_length=250, blank=True)
    feeds = models.CharField(_('feeds'),max_length=250, blank=True)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Provider:detail', kwargs={
            'id': self.id
        })


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_('name'),max_length=250)
    description = models.CharField(_('description'),max_length=250, blank=True)
    address = models.CharField(_('address'),max_length=250, blank=True)
    city = models.CharField(_('city'),max_length=100, blank=True)
    state = models.CharField(_('state'),max_length=100, blank=True)
    zipCode = models.CharField(_('zipCode'),max_length=100, blank=True)
    contacto = models.CharField(_('contacto'),max_length=100, blank=True)
    notes = models.CharField(_('notes'),max_length=250, blank=True)
    email = models.EmailField(_('email'),max_length=70, blank=True)
    phone = models.CharField(_('phone'),max_length=250, blank=True)
    url_corp = models.CharField(_('url'),max_length=250, blank=True)
    feeds = models.CharField(_('feeds'),max_length=250, blank=True)
    chefs = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    providers = models.ManyToManyField(Provider)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Restaurant:detail', kwargs={
            'id': self.id
        })



class Ingredient(models.Model):

    GRAM = "gram"
    UNIT = "unit"
    MILLILITER = "milliliter"
    KILOGRAM = "kilogram"

    PRESENTATION_CHOICES = [
        (GRAM, "Gram"),
        (UNIT, "Unit"),
        (MILLILITER, "Milliliter"),
        (KILOGRAM, "Kilogram")
    ]

    GROCERY = "grocery"
    PROTEIN = "protein"
    FRUVER = "fruVer"
    CATEGORY_CHOICES = [
        (GROCERY, "Grocery"),
        (PROTEIN, "Protein"),
        (FRUVER, "FruVer")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(_('name'),max_length=250)
    type = models.CharField(_('type'),max_length=50,choices=CATEGORY_CHOICES, default=GROCERY)
    presentation = models.CharField(_('presentation'),max_length=50,choices=PRESENTATION_CHOICES, default=GRAM)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(_('description'),max_length=999)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    qty = models.DecimalField(max_digits=20, decimal_places=10)
    provider = models.ForeignKey(Provider,null=True, on_delete=models.SET_NULL)
    chef = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    merma = models.DecimalField(max_digits=10,decimal_places=6, default=0.1)
    history = HistoricalRecords()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Ingredient:detail', kwargs={
            'id': self.id
        })


class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_('name'),max_length=100)
    description = models.CharField(_('description'),max_length=250,blank=True)
    isComplete = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=20, decimal_places=10)
    portions = models.DecimalField(max_digits=20, decimal_places=10, default=1.0)
    mpcost = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    prepacost = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    portioncost = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    mpestablish = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    errormargin = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    realratemp  = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    saleprice = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    menuprice = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    realsaleprice = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    taxportion = models.DecimalField(max_digits=20, decimal_places=10,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    items = models.ManyToManyField(Ingredient,through='Steps',through_fields=('receta','ingredient'))
    chef = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Receta:detail', kwargs={
            'id': self.id
        })


class Steps(models.Model):
   id = models.AutoField(primary_key=True)
   receta = models.ForeignKey(Receta,on_delete=models.CASCADE)
   ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
   qty = models.DecimalField(max_digits=20,decimal_places=10)
   preparacion = models.CharField(max_length=250)
   merma = models.DecimalField(max_digits=10,decimal_places=6)


   def __str__(self):
        return self.preparacion

   def get_absolute_url(self):
        return reverse('Step:detail', kwargs={
            'id': self.id
        })

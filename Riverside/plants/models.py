from django.db import models
from django.utils.html import mark_safe


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
 
    class Meta:
        db_table = 'category'
 
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
 
    class Meta:
        db_table = 'subcategory'
 
    def __str__(self):
        return self.name

class Sun_Exposure(models.Model):
    description = models.CharField(max_length=100)
 
    class Meta:
        db_table = 'sun exposure'
 
    def __str__(self):
        return self.description


class Soil_Type(models.Model):
    description = models.CharField(max_length=100)
 
    class Meta:
        db_table = 'soil type'
 
    def __str__(self):
        return self.description

class Soil_Moisture(models.Model):
    description = models.CharField(max_length=100)
 
    class Meta:
        db_table = 'soil moisture'
 
    def __str__(self):
        return self.description

class Habit(models.Model):
    description = models.CharField(max_length=100)
 
    class Meta:
        db_table = 'habit'
 
    def __str__(self):
        return self.description

class Plant(models.Model):
    variety = models.CharField(max_length=100)
    botanical_name = models.CharField(max_length=100, blank=True, null=True)
    pronunciation = models.CharField(max_length=100, blank=True, null=True)
    aliases = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=2000, blank=True, null=True)
    zone = models.IntegerField(default=0, blank=True, null=True)
    min_temp = models.CharField(max_length=10, blank=True, null=True)
    tips = models.CharField(max_length=2000, blank=True,  null=True)
    sun_exposure = models.ManyToManyField(Sun_Exposure, blank=True)
    soil_type = models.ManyToManyField(Soil_Type, blank=True)
    difficulty = models.CharField(max_length=50, blank=True, null=True)
    soil_moisture = models.ManyToManyField(Soil_Moisture, blank=True)
    habit = models.ManyToManyField(Habit, blank=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    spread = models.CharField(max_length=50, blank=True, null=True)
    growth_rate = models.CharField(max_length=50, blank=True, null=True)
    companion_plant = models.CharField(max_length=500, blank=True, null=True)
    blooming_fruiting = models.CharField(max_length=100, blank=True, null=True)
    summer_foliage = models.CharField(max_length=100, blank=True, null=True)
    fall_foliage = models.CharField(max_length=100, blank=True, null=True)
    flower_color = models.CharField(max_length=100, blank=True, null=True)
    uses_characteristics = models.CharField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    deer_resistant = models.BooleanField(default=True, blank=True, null=True)
    drought_tolerant = models.BooleanField(default=True, blank=True, null=True)
    attracts_pollinators = models.BooleanField(default=True, blank=True, null=True)
    ground_cover = models.BooleanField(default=True, blank=True, null=True)
    photo_1 = models.ImageField(upload_to='photos', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos', blank=True, null=True)
    qr_code = models.ImageField(upload_to='QR', blank=True, null=True)
    this_year = models.BooleanField(default=True, blank=True, null=True)
 
    class Meta:
        db_table = 'plant_data'
 
    def __str__(self):
        return self.variety
    
    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.qr_code.url}" width = "300"/>')


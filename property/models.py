from django.db import models
from phone_field import PhoneField

# Create your models here.

class Property_Info(models.Model):
    property_id = models.IntegerField(primary_key=True)
    property_name = models.CharField(max_length=100)
    address = models.TextField()
    landmark = models.CharField(max_length=75, null=True)
    description = models.TextField(null=True, help_text='More Information of Property - Optional')
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=6)
    point_of_contact = models.EmailField()
    poc_mobile = models.CharField(max_length=12)
    poc_name = models.CharField(max_length=100)
    telephone = PhoneField(blank=True, help_text='Contact phone number', null=True)
    # PhoneField attempts to coerce all phone numbers +[country code][number]x[extension]
    is_active = models.BooleanField(default=True)
    website = models.CharField(max_length=100, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.property_name

    def property_id(self):
        if self.property_id:
            return "P" + self.property_id
    
class Unit_types(models.Model):
    unit_type = models.CharField(max_length=25)
    area_in_sq = models.FloatField()
    descrption = models.TextField(max_length=100, verbose_name="unit_type_descrption")
    for_property = models.ForeignKey(Property_Info, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name="unit_type_is_active")

    def __str__(self):
        return self.unit_type +' ' + str(self.area_in_sq)
    

class Unit_status(models.Model):
    status = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.status

class Unit(models.Model):
    unit_no = models.CharField(max_length=5)
    wing = models.CharField(max_length=10)
    status = models.ForeignKey(Unit_status, on_delete=models.CASCADE, blank=True, null=True, default=1)
    descrption = models.TextField(max_length=100, verbose_name="unit_descrption", null=True)
    unit_type = models.ForeignKey(Unit_types, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name="unit_is_active")

    def __str__(self):
        return self.unit_no
    
    def unit_number(self):
        if self.unit_no:
            return self.wing + '-' + self.unit_no

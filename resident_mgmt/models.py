from django.db import models
from property.models import *

# Create your models here.

class Resident_info(models.Model):
    tenant_name = models.CharField(max_length=100, unique=True)
    property_id = models.ForeignKey(Property_Info, on_delete=models.CASCADE)
    unit_no = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=True)
    lease_from = models.DateField()
    lease_to = models.DateField(null=True)
    lease_renewal = models.DateField(null=True)
    move_in = models.DateField()
    move_out = models.DateField(null=True)
    tenant_status = models.CharField(max_length=25)
    roommates = models.IntegerField(null=True)
    mobile = models.CharField(max_length=12, unique=True)
    is_ref = models.BooleanField(default=False)
    ref_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    rent = models.FloatField(null=True)
    address = models.TextField()

    def __str__(self):
        return self.tenant_name
    

class ledger(models.Model):
    tenant_acc = models.AutoField(primary_key=True)
    tenant_id = models.ForeignKey(Resident_info, on_delete=models.CASCADE)

    def __str__(self):
        return self.tenant_acc

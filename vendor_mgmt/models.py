from django.db import models

# Create your models here.

class vendor_info(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=12)
    website = models.CharField(max_length=25, null=True)
    email = models.EmailField(verbose_name="Vendor Email", null=True)
    service = models.CharField(max_length=50)
    property_id = models,models.ForeignKey("property.Property_Info", verbose_name="For Property", on_delete=models.CASCADE)
    helpline_no = models.CharField(max_length=15)

    def __str__(self):
        return self.vendor_name

class vendor_invoices(models.Model):
    v_invoice_id = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey(vendor_info, on_delete=models.CASCADE)
    bill_no = models.CharField(max_length=15)
    bill_date = models.DateField()
    due_date = models.DateField(null=True)
    service_from = models.DateField()
    service_to = models.DateField()
    charges = models.FloatField()
    billing_month = models.CharField(max_length=12)

    def __str__(self):
        return self.bill_no


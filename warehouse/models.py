from django.db import models


# Create your models here.

class carton_cloud_client(models.Model):
    c_id = models.CharField(max_length=32, unique=True)
    c_name = models.CharField(max_length=64)
    c_email = models.CharField(max_length=128)
    c_telephone = models.CharField(max_length=64)
    c_customer_charge_name = models.CharField(max_length=32)
    c_active = models.CharField(max_length=32)
    c_register_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def createClients(cls, c_id, c_name, c_email, c_telephone, c_customer_charge_name, c_active):
        return cls(c_id, c_name, c_email, c_telephone, c_customer_charge_name, c_active)


class containers(models.Model):
    ctnr_number = models.CharField(max_length=64)
    ctnr_type = models.CharField(max_length=32)
    ctnr_eta = models.DateField()
    ctnr_owner = models.CharField(max_length=128)
    ctnr_job = models.CharField(max_length=64)
    ctnr_special = models.CharField(max_length=128)

    @classmethod
    def createContiainers(cls, ctnr_number, ctnr_type, ctnr_eta, ctnr_owner, ctnr_job, ctnr_special):
        return cls(ctnr_number, ctnr_type, ctnr_eta, ctnr_owner, ctnr_job, ctnr_special)


class location_used(models.Model):
    l_details = models.CharField(max_length=256)
    l_time = models.DateField(auto_now_add=True)

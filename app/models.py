from django.db import models


# Create your models here.

class Clients(models.Model):
    clientCompanyID = models.AutoField
    clientCompanyCreditRating = models.CharField(max_length=16, default='10', null=True)
    clientCompanyName = models.CharField(max_length=128, unique=True)
    clientCompanyContactPerson = models.CharField(max_length=64, default='0', null=True)
    clientCompanyContactMobile = models.CharField(max_length=64, default='0')
    clientCompanyAddress = models.CharField(max_length=128, default='NZ')
    clientCompanyEmail = models.CharField(max_length=128, default='0')
    clientCompanyServiceOnHold = models.BooleanField(default=False, null=True)
    NZBN = models.CharField(max_length=64, unique=True, default='0')

    @classmethod
    def createClients(cls, clientCompanyName, clientCompanyContactPerson, clientCompanyEmail,
                      clientCompanyContactMobile, clientCompanyAddress, NZBN):
        return cls(clientCompanyName, clientCompanyContactPerson, clientCompanyEmail, clientCompanyContactMobile,
                   clientCompanyAddress, NZBN)


class Meta:
    db_table = 'Clientslist'

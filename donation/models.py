from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=115, null=True)
    address = models.CharField(max_length=300, null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null= True)
    address = models.CharField(max_length=300, null= True)
    userpic = models.FileField(null= True)
    idpic = models.FileField(null= True)
    aboutme = models.CharField(max_length=300, null= True)
    status = models.CharField(max_length=20, null= True)
    adminremark = models.CharField(max_length=300, null= True)
    updateiondate = models.DateField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class DonationArea(models.Model):

    areaname = models.CharField(max_length=15, null= True)
    discription = models.CharField(max_length=300, null= True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.areaname

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donationname = models.CharField(max_length=100, null=True)
    collectionloc = models.CharField(max_length=300, null=True)
    donor_contact = models.CharField(max_length=15, null=True)
    ngo_contact = models.CharField(max_length=15, null=True)
    val_contact = models.CharField(max_length=15, null=True)
    deliveryloc = models.CharField(max_length=300, null=True)
    donationpic = models.FileField(null=True)

    description = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=50, null=True)
    updationdate = models.DateField(null=True)
    ngoname = models.CharField(max_length=300, null=True)
    valname = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.id)

class Gallery(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class NGO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null= True)
    address = models.CharField(max_length=300, null= True)
    userpic = models.FileField(null= True)
    idpic = models.FileField(null= True)
    aboutme = models.CharField(max_length=300, null= True)
    status = models.CharField(max_length=20, null= True)
    adminremark = models.CharField(max_length=300, null= True)
    updateiondate = models.DateField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
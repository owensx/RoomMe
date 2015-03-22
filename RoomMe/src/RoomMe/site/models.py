from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.forms import ModelForm

from filer.fields.image import FilerImageField

# Create your models here.
class Listing(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    price = models.FloatField()
    dateAvailable = models.DateField()
#     img1 = FilerImageField(null=True, blank=True,
#                            related_name="img1")
#     img2 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img3 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img4 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img5 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img6 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img7 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img8 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img9 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
#     img10 = models.ImageField(blank=True, upload_to='/static/imgs/listings/')
    perks = models.CharField(max_length = 200)
    roomieIds =  models.CharField(max_length = 200)
    
    def __str__(self):
        return self.id.__str__()
    
class Roomie(models.Model):    
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User)
    occupation = models.CharField(max_length = 200)
    currentCity = models.CharField(max_length = 200)
      
    def __str__(self):
        return self.user.__str__()


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'address', 'price', 'dateAvailable', 'perks']
        
 
#create a profile whenever a user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        idToInsert = uuid4().int % 1000000000
        while Roomie.objects.filter(id=idToInsert):
            idToInsert = uuid4().int % 1000000000
                
        roomie = Roomie(id=idToInsert, user=instance)
        roomie.save()
        
post_save.connect(create_profile, sender=User)
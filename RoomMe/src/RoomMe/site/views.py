from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate

from uuid import uuid4
from django.contrib.auth.models import User
from RoomMe.site.models import Listing
from RoomMe.site.models import ListingForm
from RoomMe.site.models import Roomie

from django.core.files import File

import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def loginUser(request):
    logout(request)
    
    User.objects.create_user('newnew1112221', '', 'pass')
    user2 = authenticate(username='newnew1112221', password='pass')
   
    login(request, user2)
     
    return HttpResponseRedirect('/roomie/' + request.user.roomie.id.__str__())

def createProfile(request):
    return

def listing(request, listingId):
    listing = get_object_or_404(Listing ,pk=listingId)
    
    #get associated profiles
    roomies = []
    roomieIds = listing.roomieIds.split('!')
    
    for roomieId in roomieIds:
        if roomieId != '':
            try:
                roomie = Roomie.objects.get(pk=roomieId)
                roomies.append(roomie)
                
            except Roomie.DoesNotExist:
                #send email saying a listing wanted a nonexistant profile
                pass
    
    #create listing images URLs
#     fullImgUrls = []
#     imgUrls = listing.imgUrls.split('!')
#     
#     for imgUrl in imgUrls:    
#         fullImgUrls.append("imgs/listings/"+imgUrl.__str__())
    
    context = {
               'id' : listing.id
               , 'name' : listing.name
               , 'address' : listing.address
               , 'price' : listing.price
               , 'dateAvailable' : listing.dateAvailable
               #, 'imgUrls' : fullImgUrls
               , 'perks' : listing.perks.split('!')
               , 'roomies' : roomies
               }
    
    return render(request, 'listings/listing.html', context)

def roomie(request, roomieId):
    roomie = get_object_or_404(Roomie ,id=roomieId)
    
    #get associated listings
    listings = []
    listingIds = roomie.listingIds.split('!')
    
    for listingId in listingIds:
        if listingId != '':
            try:
                listing = Listing.objects.get(id=listingId)
                listings.append(listing)
                
            except Listing.DoesNotExist:
                #send email saying a profile wanted a nonexistant listing
                pass
    
    #create roomie images URLs
    fullImgUrls = []
    imgUrls = listing.imgUrls.split('!')
    for imgUrl in imgUrls:    
        fullImgUrls.append("roomies/imgs/"+imgUrl)
    
    context = {
               'id' : roomie.id
               , 'occupation' : roomie.occupation
               , 'currentCity' : roomie.currentCity
               , 'imgUrls' : fullImgUrls
               }
    
    return render(request, 'roomies/roomie.html', context)

def addListing(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ListingForm(request.POST, request.FILES) # A form bound to the POST data
        
        if form.is_valid():
            print(form.cleaned_data['name'])
           
           # print("hrywsdfdsfsddwdw")
            #handleOpenn(request.FILES['img1'])
            #form.save()
            idToInsert = uuid4().int % 1000000000
            while Listing.objects.filter(id=idToInsert):
                idToInsert = uuid4().int % 1000000000
                
            listing = Listing(id=idToInsert
                              , name=form.cleaned_data['name']
                              , address=form.cleaned_data['address']
                              , price=form.cleaned_data['price']
                              , dateAvailable=form.cleaned_data['dateAvailable']
                              , img1=request.FILES['img1']
                              , perks=form.cleaned_data['perks']
                              , roomieIds='')
            
            listing.save()
            return HttpResponseRedirect('/listing/' + idToInsert.__str__()) # Redirect after POST
        else:
            raise Http404("form bad")
    else:
        form = ListingForm()
        context = {'form': form}
        
    return render(request, 'listings/addListing.html', context)

def addListingPics(request):
    print("s")
    if request.method == 'POST':
        #print(request.FILES['file'].url)
        data = request.FILES['file']
        path = default_storage.save('/static/imgs/listings/' + str(data), ContentFile(data.read()))
        #tmp_file_path = os.path.join(settings.MEDIA_ROOT, path)
    return render(request, 'listings/addListingPics.html')

    
@login_required
def addUserToListing(request, listingId):
    listing = Listing.objects.get(id=listingId)
    listing.roomieIds = listing.roomieIds + request.user.roomie.id.__str__() + "!"
    listing.save()
    
    return

def handle_uploaded_file(file):
    with open('/static/listings/imgs/blanks.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            
def handleOpenn(file):
    with open('/static/imgs/listings/'+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RoomMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^listing/(?P<listingId>\d+)/$'
        , 'RoomMe.site.views.listing', name='listing'),
    url(r'^roomie/(?P<roomieId>\d+)/$'
        , 'RoomMe.site.views.roomie', name='roomie'),
    url(r'^addUserToListing/(?P<listingId>\d+)/$'
        , 'RoomMe.site.views.addUserToListing', name='addUserToListing'),
                       
    url(r'^addListing.html$', 'RoomMe.site.views.addListing', name='addListing'),
    url(r'^addListingPics.html$', 'RoomMe.site.views.addListingPics', name='addListingPics'),
    url(r'^login/', 'RoomMe.site.views.loginUser', name='loginUser'),
)

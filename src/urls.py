from django.contrib import admin
from django.urls import path
from login.views import (
    loginView, loginOptionsView, loginNumberView,
    loginOtpError, loginOtpVerify, loginLocation
)  
from profilesBasic.views import (
    profileBasic, profileAdvanced,
    managePhotos , selectSource,
    aboutYou
) 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    #login endpoints
    path('login/', loginView),
    path('login/options', loginOptionsView),
    path('login/number', loginNumberView),
    path('login/number/otp', loginOtpVerify),
    path('login/number/otp/error', loginOtpError),   
    path('login/location', loginLocation),  

    #profile basic endpoints
    path('profile/basic', profileBasic),
    path('profile/advanced', profileAdvanced),
    path('profile/photos', managePhotos),
    path('profile/photos/source', selectSource),
    path('profile/about', aboutYou)
    
]

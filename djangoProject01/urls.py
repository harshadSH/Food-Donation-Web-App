"""djangoProject01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from donation.views import *
from donation.views import donate_now
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_logins, name='all_logins'),
    path('donor_login', donor_login, name='donor_login'),
    path('volunteer_login', volunteer_login, name='volunteer_login'),
    path('ngo_login', ngo_login, name='ngo_login'),
    path('donor_reg', donor_reg, name='donor_reg'),
    path('donor_base', donor_base, name='donor_base'),
    path('foram', foram, name='foram'),
    path('donate_now', donate_now, name='donate_now'),
    path('donor_history', donor_history, name='donor_history'),
    path('ngo_reg', ngo_reg, name='ngo_reg'),
    path('ngo_base', ngo_base, name='ngo_base'),
    path('pending_donation', pending_donation, name='pending_donation'),
    path('accepted_donation', accepted_donation, name='accepted_donation'),
    path('volunteer_reg', volunteer_reg, name='volunteer_reg'),
    path('volunteer_base', volunteer_base, name='volunteer_base'),
    path('available_order', available_order, name='available_order'),
    path('vol_history', vol_history, name='vol_history'),
    path('ngo_history', ngo_history, name='ngo_history'),

    path('pending_order', pending_order, name='pending_order'),
    path('donation_detail/<int:pid>', donation_detail, name='donation_detail'),
    path('view_detail/<int:pid>', view_detail, name='view_detail'),
    path('logout/', Logout, name='logout'),
    

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

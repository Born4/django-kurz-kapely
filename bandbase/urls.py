"""
URL configuration for coderslab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from bandbase.views import data_odeslana_data_ok, data_odeslana_bad_data, home_page
from bands.views import AccountLoginConfirmationView, AccountLogoutConfirmationView, AccountLoginView, \
    AccountLogoutView, AccountLogoutYesNoView, SessionListParametersView, BandAboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Account authentication
    path('accounts/login/', AccountLoginView.as_view(), name='account-login'),
    path('logout/', AccountLogoutView.as_view(), name='account-logout'),
    path('loginconfirmation/', AccountLoginConfirmationView.as_view(), name='confirm-login'),
    path('logoutconfirmation/', AccountLogoutConfirmationView.as_view(), name='confirm-logout'),
    path('logout-yes-no/', AccountLogoutYesNoView.as_view(), name='logout-yes-no'),
    # Session management
    path('listsession/', SessionListParametersView.as_view(), name='session-list'),
    # Exercise - aplikace
    path('bands/', include("bands.urls", namespace="bands")),
    # Service views
    path('ok-data/', data_odeslana_data_ok, name="ok-data"),
    path('bad-data/', data_odeslana_bad_data, name="bad-data"),
    # path('', home_page, name='home'),
    path('', BandAboutView.as_view(), name='home-page'),
]

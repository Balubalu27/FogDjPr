from django.urls import path

from address.views import AddressFromApiList

urlpatterns = [
    path('', AddressFromApiList.as_view(), name='home'),
]

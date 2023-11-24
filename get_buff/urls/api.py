from django.urls import path, include

from account.urls import urlpatterns as account_urlpattern

app_name = "api"

urlpatterns = [
    path('',include((account_urlpattern, 'account'), namespace='account'))
]

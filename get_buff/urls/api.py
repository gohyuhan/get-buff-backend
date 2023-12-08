from django.urls import path, include

from account.urls import urlpatterns as account_urlpattern
from training.urls import urlpatterns as training_urlpattern
from user.urls import urlpatterns as user_urlpattern

app_name = "api"

urlpatterns = [
    path('account/',include((account_urlpattern, 'account'), namespace='account')),
    path('training/',include((training_urlpattern, 'training'), namespace='training')),
    path('user/',include((user_urlpattern, 'user'), namespace='user'))
]

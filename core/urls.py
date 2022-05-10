from django.urls import path, re_path
from .views import * 

urlpatterns = [
    path("initiate", initiate_payment, name='initiate'),
    path("verify/<str:ref>", verify_payment, name="verify"),
]

urlpatterns +=[
    path('getkey', getSecretKey)
]

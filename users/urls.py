from django.urls import path

from users.views import login, edit, registration


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),    
    path('registration/', registration, name='registration'),
    path('edit/', edit, name='edit'),
]
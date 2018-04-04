from django.conf.urls import url

from .views import register

app_name = 'register'
urlpatterns = [
    url(r'',register,name='register')
]
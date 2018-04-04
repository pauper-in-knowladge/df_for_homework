from django.conf.urls import url
from .views import login

app_name = 'login'

urlpatterns = [
    url(r'',login,name='login')
]
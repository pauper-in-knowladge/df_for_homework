from django.conf.urls import url

from .views import *

app_name = 'management'

urlpatterns = [
    url(r'',show_students,name='show_students'),
    # url(r'',add_stu,name='add_stu'),

]
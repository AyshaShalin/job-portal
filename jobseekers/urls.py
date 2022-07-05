from django.urls import path
from . import views

app_name='jobskr'

urlpatterns=[ 
    path('',views.login,name='login'),
    path('search job',views.searchjob,name='search'),
    path('job details',views.jobdetails,name='details'),
]
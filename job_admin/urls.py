from django.urls import path
from . import views
app_name="jadmin"

urlpatterns=[ 
    path('login',views.login,name="login"),
    path('view emp',views.view,name="view")
]
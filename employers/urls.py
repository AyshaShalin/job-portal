from django.urls import path
from . import views
app_name='employer'


urlpatterns=[  
    path('login',views.login,name="login"),
    path('Dashboard',views.dashboard,name="dashboard"),
    path('SignUp',views.signup,name="sign")
]
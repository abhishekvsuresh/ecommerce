from django.urls import path
from . import views

urlpatterns = [
 path('', views.log,name='login'),
 path('reg', views.reg,name='reg'),
 path('home', views.home,name='home'),

 path('login_btn', views.log_btn),
 path('register',views.register)

]
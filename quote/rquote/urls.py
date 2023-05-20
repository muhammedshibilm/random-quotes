from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="home"),
    path('api/quote/',views.random_quote, name='random_quote'),    
]

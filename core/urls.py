from django.urls import path
from .views import home
from . import views
app_name = "core"



urlpatterns =[
         path('', home, name='home'), 
        path('contact/', views.contact_view, name='contact'), 
    path('email/', views.email_view, name='email'),
]
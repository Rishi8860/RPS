import imp
from django.urls import path
from website import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('doctors',views.doctor,name='doctor'),
    path('About',views.about,name='about'),
    path('Touch',views.get_in_touch,name='touch'),
    path('Founders',views.founders,name='founders'),
]
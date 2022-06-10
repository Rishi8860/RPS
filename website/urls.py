from django.contrib import admin
from django.urls import path
from website import views
# admin header
admin.site.site_header="RPS GLOBAL HOSPITALS"
admin.site.site_title="RPS ADMIN"
admin.site.index_title="RPS GLOBAL ADMIN"
urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),
    path('doctors',views.doctor,name='doctor'),
    path('About',views.about,name='about'),
    path('Touch',views.get_in_touch,name='touch'),
    path('Founders',views.founders,name='founders'),
    path('carriers',views.carriers,name='carriers'),
    path('Resume',views.Resume,name='Resume')
]
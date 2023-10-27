from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "AcademiSync Admin"
admin.site.site_title = "AcademiSync Admin Portal"
admin.site.index_title = "Welcome to AcademiSync"
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("service",views.service,name='service'),
    path("contact",views.contact,name='contact'),
    path("forgot",views.forgot,name='forgot'),
    path("register",views.register,name='register'),
    
    path("upload",views.upload,name='upload'),
    path("sign",views.sign,name='sign')
]
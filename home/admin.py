from django.contrib import admin
from home.models import Contact,Register,Usname,Password_Configuration
# Register your models here.
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Usname)
admin.site.register(Password_Configuration)

from django.contrib import admin
from myapp.models import ca
from myapp.models import login
from myapp.models import register

admin.site.register(ca)
admin.site.register(login)
admin.site.register(register)    


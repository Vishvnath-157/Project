from django.contrib import admin
from home.models import Contact
from home.models import Signup
from home.models import Login
from home.views import output
# Register your models here.
admin.site.register(Contact)
admin.site.register(Signup)
admin.site.register(Login)

from django.contrib import admin
from . models import Login_info,SignUp_info,Cart_info,Products,Admin,Contact


admin.site.register(Login_info)

admin.site.register(SignUp_info)
admin.site.register(Cart_info)
admin.site.register(Products)
admin.site.register(Admin)
admin.site.register(Contact)



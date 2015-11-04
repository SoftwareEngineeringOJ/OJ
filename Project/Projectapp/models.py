from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class Userdetails(models.Model):
    username = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','username')
class UserdetailsAdmin(admin.ModelAdmin):
    list_display = ('username','rank')

admin.site.register(User,UserAdmin)
admin.site.register(Userdetails,UserdetailsAdmin)
from django.db import models
from django.contrib import admin
# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    signature = models.TextField(max_length=200)
    school = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    register_time= models.DateTimeField()

class group(models.Model):
    groupname = models.CharField(max_length=50)
    groupmembers = models.ManyToManyField(user)
    register_time= models.DateTimeField()


class problemslist(models.Model):
    OJ = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    ratio = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    time_limit = models.CharField(max_length=15)
    mem_limit = models.CharField(max_length=15)
    description = models.TextField()
    inputs = models.TextField()
    output = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    hint = models.TextField()

class group_status(models.Model):
	problemsID = models.CharField(max_length=100)
	groupID = models.CharField(max_length=30)
	groupname = models.CharField(max_length=50)
	sumrank = models.CharField(max_length=50)
	competedate = models.DateTimeField()
	codes = models.TextField()
	is_codes_private = models.BooleanField()
	is_group_private = models.BooleanField()
	submit_time = models.DateTimeField() 

class user_status(models.Model):
	problemID = models.CharField(max_length=15)
	problemTitle = models.CharField(max_length=35)
	userID = models.CharField(max_length=20)
	username = models.CharField(max_length=50)
	OJ = models.CharField(max_length=10)
	result = models.CharField(max_length=30)
	memory = models.CharField(max_length=15)
	time = models.CharField(max_length=15)
	language = models.CharField(max_length=10)
	code = models.TextField()
	submit_time = models.DateTimeField()
	is_code_private = models.BooleanField()
	is_user_private = models.BooleanField()

class user_management(models.Model): 
	userID = models.CharField(max_length=20)
	username = models.CharField(max_length=50)
	joined_groups = models.ManyToManyField(group)

class discussion(models.Model):
	userID = models.CharField(max_length=20)
	username = models.CharField(max_length=50)
	problemID = models.CharField(max_length=15)
	problemTitle = models.CharField(max_length=35)
	speak = models.TextField(max_length=300)


class useradmin(admin.ModelAdmin):
    list_display = ('username','register_time')
class groupadmin(admin.ModelAdmin):
    list_display = ('groupname','register_time')
class user_statusadmin(admin.ModelAdmin):
    list_display = ('username','submit_time')
class group_statusadmin(admin.ModelAdmin):
    list_display = ('groupname','submit_time')
class problemslistadmin(admin.ModelAdmin):
    list_display = ('OJ','title')
class user_managementadmin(admin.ModelAdmin):
    list_display = ('username','username')
class discussionadmin(admin.ModelAdmin):
    list_display = ('problemTitle','username')


admin.site.register(user,useradmin)
admin.site.register(group,groupadmin)
admin.site.register(user_status,user_statusadmin)
admin.site.register(group_status,group_statusadmin)
admin.site.register(problemslist,problemslistadmin)
admin.site.register(user_management,user_managementadmin)
admin.site.register(discussion,discussionadmin)

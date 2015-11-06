from django.db import models
from django.contrib import admin
# Create your models here.

class User(models.Model): 
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Status(models.Model):
    username = models.CharField(max_length=50)
    statu = models.CharField(max_length=10) #right or wrong
    submittime = models.DateTimeField()
    runningtime = models.CharField(max_length=10) 
    memory = models.CharField(max_length=10) 

class HOJ_Problems(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    problem = models.TextField()
    category = models.CharField(max_length=50)
    dificulty =  models.CharField(max_length=50)
class POJ_Problems(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    problem = models.TextField()
    category = models.CharField(max_length=50)
    dificulty =  models.CharField(max_length=50)
class ZOJ_Problems(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    problem = models.TextField()
    category = models.CharField(max_length=50)
    dificulty =  models.CharField(max_length=50)
class NOJ_Problems(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    problem = models.TextField()
    category = models.CharField(max_length=50)
    dificulty =  models.CharField(max_length=50)
class TYVJ_Problems(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    problem = models.TextField()
    category = models.CharField(max_length=50)
    dificulty =  models.CharField(max_length=50)

class Userdetail(models.Model): 
    username = models.CharField(max_length=50)
    precision = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    algorithm = models.CharField(max_length=10)
    speed = models.CharField(max_length=10)
    sumrank = models.CharField(max_length=50)
    HOJ = models.ManyToManyField(HOJ_Problems)
    POJ = models.ManyToManyField(POJ_Problems)
    ZOJ = models.ManyToManyField(ZOJ_Problems)
    NOJ = models.ManyToManyField(NOJ_Problems)
    TYVJ = models.ManyToManyField(TYVJ_Problems)

class Groupdetail(models.Model):
    groupname = models.CharField(max_length=50)
    sumrank = models.CharField(max_length=50)
    competedate = models.DateTimeField()

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','username')
class UserdetailAdmin(admin.ModelAdmin):
    list_display = ('username','sumrank')
class GroupdetailAdmin(admin.ModelAdmin):
    list_display = ('groupname','sumrank')
class StatusAdmin(admin.ModelAdmin):
    list_display = ('username','statu')
class HOJ_ProblemsAdmin(admin.ModelAdmin):
    list_display = ('title','category')
class POJ_ProblemsAdmin(admin.ModelAdmin):
    list_display = ('title','category')
class ZOJ_ProblemsAdmin(admin.ModelAdmin):
    list_display = ('title','category')
class NOJ_ProblemsAdmin(admin.ModelAdmin):
    list_display = ('title','category')
class TYVJ_ProblemsAdmin(admin.ModelAdmin):
    list_display = ('title','category')

admin.site.register(User,UserAdmin)
admin.site.register(Userdetail,UserdetailAdmin)
admin.site.register(Groupdetail,GroupdetailAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(HOJ_Problems,HOJ_ProblemsAdmin)
admin.site.register(POJ_Problems,POJ_ProblemsAdmin)
admin.site.register(ZOJ_Problems,ZOJ_ProblemsAdmin)
admin.site.register(NOJ_Problems,NOJ_ProblemsAdmin)
admin.site.register(TYVJ_Problems,TYVJ_ProblemsAdmin)

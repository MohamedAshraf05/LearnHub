from django.contrib import admin
from .models import Teachers , Courses
# Register your models here.


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number' , 'Custom_id' , 'id')
    ordering = ['id']

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name' ,'teacher' ,'Custom_id' , 'id')
    ordering = ['id']
from django.contrib import admin
from .models import myPetText, Comment

class MyPetAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")

class MyPetCommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "comments")

admin.site.register(myPetText, MyPetAdmin)
admin.site.register(Comment, MyPetCommentAdmin)
# Register your models here.

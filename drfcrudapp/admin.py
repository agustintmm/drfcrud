from django.contrib import admin
from .models import *


# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')    

class CursoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  

admin.site.register(Producto, ProductoAdmin)      
admin.site.register(Post, PostAdmin)      
admin.site.register(Curso, CursoAdmin) 
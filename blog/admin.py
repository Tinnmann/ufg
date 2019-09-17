from django.contrib import admin
from blog.models import BlogPost, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, PostAdmin)
admin.site.register(Category, CategoryAdmin)

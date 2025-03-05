from django.contrib import admin


from .models import Category, News

# admin.site.register(Category)
# admin.site.register(News)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'status']
    list_filter = ['status', 'publish_time', 'category']
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


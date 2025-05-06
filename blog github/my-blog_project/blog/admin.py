from django.contrib import admin
from .models import Post, Category, Tag 
from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'created_at', 'status')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'status')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('categories', 'tags')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fields = ('title', 'slug', 'content', 'image', 'categories', 'tags', 'status', 'created_at', 'updated_at')
    filter_horizontal = ('categories', 'tags')

admin.site.register(Post, PostAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # Slug otomatik oluşturulur

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Admin panelinde gösterilecek alanlar
    prepopulated_fields = {'slug': ('name',)}  # Slug alanını name alanından otomatik doldur
    search_fields = ('name',)  # Otomatik tamamlama için gerekli
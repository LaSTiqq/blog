from django.contrib import admin
from .models import Blog, BlogTag
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe


class BlogAdmin(TranslationAdmin, admin.ModelAdmin):
    fields = ('tag', 'title', 'slug', 'preview_text', 'content', 'published')
    list_display = ('tag', 'title', 'published')
    list_editable = ('published',)
    list_display_links = ('title',)

    prepopulated_fields = {'slug': ('title_en',), }


class BlogTagAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'get_image')
    readonly_fields = ('get_image',)
    list_display = ('name', 'get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" width="75">')
    get_image.short_description = 'Miniature'


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogTag, BlogTagAdmin)

admin.site.site_title = 'Blog'
admin.site.site_header = 'Blog'

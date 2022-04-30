from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe

class BlogAdmin(TranslationAdmin, admin.ModelAdmin):
	fields = ('tag', 'title', 'slug', 'preview_text', 'content', 'keywords', 'published', 'preview_image', 'get_image')
	readonly_fields = ('get_image',)
	list_display = ('tag', 'title', 'get_image', 'published')
	list_editable = ('published',)
	list_display_links = ('title',)

	prepopulated_fields = {'slug': ('title_en',),}

	def get_image(self, obj):
		return mark_safe(f'<img src="{obj.preview_image}" width="75">')
	get_image.short_description = 'Миниатюра'

class BlogTagAdmin(admin.ModelAdmin):
	fields = ('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogTag, BlogTagAdmin)

admin.site.site_title = 'Блог'
admin.site.site_header = 'Блог'
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
	tag = models.ForeignKey('BlogTag', on_delete=models.SET_NULL, null=True, verbose_name='Тэг')
	title = models.CharField(max_length=120, verbose_name='Заголовок')
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	content = RichTextUploadingField(config_name='special', verbose_name='Контент')
	preview_image = models.URLField(verbose_name='Картинка предпросмотра (ссылка)')
	preview_text = models.TextField(verbose_name='Текс предпросмотра')
	published = models.BooleanField(default=False, verbose_name='Опубликовано')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog_detail', kwargs={'slug': self.slug})

	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Записи'
		ordering = ['-id']

class BlogTag(models.Model):
	name = models.CharField(max_length=72, db_index=True, verbose_name='Имя тэга')

	def get_absolute_url(self):
		return reverse('tag', kwargs={'tag_id': self.pk})

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тэг'
		verbose_name_plural = 'Тэги'
		ordering = ['id']
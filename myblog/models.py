from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Blog(models.Model):
    tag = models.ForeignKey(
        'BlogTag', on_delete=models.SET_NULL, null=True, verbose_name='Tag')
    title = models.CharField(max_length=120, verbose_name='Title')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    content = RichTextField(config_name='special', verbose_name='Content')
    preview_text = models.TextField(verbose_name='Preview text')
    published = models.BooleanField(default=False, verbose_name='Published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:blog_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
        ordering = ['-id']


class BlogTag(models.Model):
    name = models.CharField(max_length=72, db_index=True,
                            verbose_name='Tag name')
    image = models.URLField(verbose_name='Preview image')

    def get_absolute_url(self):
        return reverse('myblog:tag', kwargs={'tag_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['id']

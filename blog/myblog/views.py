from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog, BlogTag

class MainView(TemplateView):
    template_name = 'myblog/index.html'

class BlogList(ListView):
	model = Blog
	template_name = 'myblog/blog_list.html'
	context_object_name = 'blog'
	paginate_by = 10

class BlogByTag(ListView):
	model = Blog
	template_name = 'myblog/blog_list_by_tag.html'
	context_object_name = 'blog'
	allow_empty = False
	paginate_by = 10

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = BlogTag.objects.get(pk=self.kwargs['tag_id'])
		return context

	def get_queryset(self):
		return Blog.objects.filter(tag_id=self.kwargs['tag_id']).select_related('tag')

class BlogDetail(DetailView):
	model = Blog
	context_object_name = 'blog'
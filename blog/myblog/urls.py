from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap
from django.urls import path
from .views import MainView, BlogList, BlogByTag, BlogDetail

app_name = 'myblog'

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('', MainView.as_view(), name='home'),
	path('blog/', BlogList.as_view(), name='blog'),
	path('blog/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
	path('tag/<int:tag_id>', BlogByTag.as_view(), name='tag'),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
]
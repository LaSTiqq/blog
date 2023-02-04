from django.urls import path
from .views import MainView, BlogList, BlogByTag, BlogDetail, Portfolio

app_name = 'myblog'

urlpatterns = [
    path('', MainView.as_view(), name='home'),
	path('blog/', BlogList.as_view(), name='blog'),
	path('blog/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
	path('portfolio/', Portfolio.as_view(), name='portfolio'),
	path('tag/<int:tag_id>', BlogByTag.as_view(), name='tag'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^words/(?P<language>\w+)/$',views.GetByLanguage.as_view(),name="word_list"), # for /api/words/en/  all words in english
	url(r'^words/(?P<language>\w+)/title__startswith=(?P<symbol>\w+)/$', views.GetByTitle.as_view(), name="get_by_title"),
	url(r'^words/(?P<language>\w+)/(?P<pk>\d+)/$', views.GetById.as_view(), name="get_by_id"),
	#url(r'^words/(?P<language>\w+)/(?P<pk>\d+)/translate=(?P<symbol>\w+)/$', views.GetTranslateById.as_views(), 
	#																		 name="get_translate_by_id"),
]
from django.conf.urls import url
from user_comments import views

urlpatterns = [
	url(r'^create/$', views.create, name='create'),
	url(r'^update/$', views.update, name='update'),
	url(r'^delete/$', views.delete, name='delete'),
	url(r'^details/$', views.details, name='details'),
	url(r'^home/$', views.stats, name='stats'),
]
"""NOT YET COMPLETED"""
handler404 = 'user_comments.views.handler404'
handler500 = 'user_comments.views.handler500'
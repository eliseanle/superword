from django.conf.urls import patterns
from django.conf.urls import url

from django.conf import settings

from superword.views import HomeView
from wordplay.views import AddView
from wordplay.views import QuizView
from wordplay.views import WordJaxView


urlpatterns = patterns(
    '',
    url(r'add/delete_word/', WordJaxView.as_view()),
    url(r'add/', AddView.as_view()),
    url(r'quiz/', QuizView.as_view()),
    url(r'^$', HomeView.as_view()),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT})
)

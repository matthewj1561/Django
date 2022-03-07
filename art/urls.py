from django.urls import path

from . import views
app_name = 'art'
urlpatterns = [
    # ex: /art/
    path('', views.index, name='index'),
    # ex: /art/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /art/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /art/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),


]

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add-question/', views.AddQuestionView.as_view(), name='add-question'),
    path('add-choice/<int:pk>/', views.AddChoicesView.as_view(), name='add-choice'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('new-question/', views.add_questions_choices_view, name='new-question')
]

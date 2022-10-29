from django.urls import path

from .views import index, vote

app_name = 'candidates'


urlpatterns = [
    path('', index, name='index'),
    path('vote/<int:candidate_id>', vote, name='vote')
]

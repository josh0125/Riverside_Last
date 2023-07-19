from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexPage, name='index'),
    path('plant-details', views.plantPage, name='plants'),
    path('category', views.categoryPage, name='categories'),
    path('contact', views.contactPage, name='contact'),

    path('error', views.error_404, name='error'),
    path('error/search', views.searchPage, name='search'),

    path('search', views.searchPage, name='search'),
    path('plant-details/search', views.searchPage, name='search'),

    path('category/search', views.searchPage, name='search'),
    path('plant-details/<int:iID>', views.onePlantDisplayPage, name='plant'),

    path('category/<str:sName>', views.categoryDisplayPage, name='category'),

    path('tags', views.tagPage, name='tag'),
    path('searchtags', views.searchTagPage, name='searchtags'),
]
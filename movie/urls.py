from django.urls import path
from .views import MovieListCreateView, MovieDetailView, AllMoviewsListView, MovieDeleteView, MovieUpdateView

urlpatterns =[
    path('movies', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/all/', AllMoviewsListView.as_view(), name='all-movie-list'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/update/<int:pk>/', MovieUpdateView.as_view(), name='move-update'),
]
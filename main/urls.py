from django.urls import path, include
from rest_framework import routers

from .views import FilmViewSet, main_view, GenresViewSet, CountriesViewSet

app_name = 'main'

router = routers.SimpleRouter()
router.register(r'films', FilmViewSet)
router.register(r'genres', GenresViewSet)
router.register(r'countries', CountriesViewSet)


urlpatterns = [
    path('', main_view),
    path('api/', include(router.urls))
]
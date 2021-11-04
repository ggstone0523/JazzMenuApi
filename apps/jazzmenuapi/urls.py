from django.urls import path
from django.urls.conf import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('jazzcategorys/', views.JazzCategoryList.as_view()),
    path('jazzcategorys/<int:pk>/', views.JazzCategoryDetail.as_view()),
    path('genre/', views.GenreList.as_view()),
    path('genre/<int:pk>/', views.GenreDetail.as_view()),
    path('region/', views.RegionList.as_view()),
    path('region/<int:pk>/', views.RegionDetail.as_view()),
    path('character/', views.CharacterList.as_view()),
    path('character/<int:pk>/', views.CharacterDetail.as_view()),
    path('era/', views.EraList.as_view()),
    path('era/<int:pk>/', views.EraDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
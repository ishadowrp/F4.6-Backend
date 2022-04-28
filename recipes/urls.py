from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RecipeAPIView, CategoryAPIView, RecipePhotoUpload

router = SimpleRouter()
router.register('recipes', RecipeAPIView, basename='recipes')
router.register('categories', CategoryAPIView, basename='profiles')

urlpatterns = router.urls
urlpatterns.append(path('recipes/upload/', RecipePhotoUpload.as_view()),)

urlpatterns = format_suffix_patterns(urlpatterns)


# urlpatterns = [
#     path('recipes/', RecipeAPIView.as_view()),
#     path('categories/', CategoryAPIView.as_view()),
# ]


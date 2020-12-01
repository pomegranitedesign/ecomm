from django.urls import path
from .views import details, index

urlpatterns = [
    path('', name='home', view=index),
    path('<int:product_id>/', name='details', view=details),
]

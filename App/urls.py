from django.urls import path
from .views import home_page, MyDetailView

urlpatterns = [
    path('', home_page),
    path('books/<int:pk>', MyDetailView.as_view(), name='mydetail')
]

from django.contrib import admin
from django.urls import path
from rentrv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RvListView.as_view()),
    path('rv/<int:pk>', views.RvDetailView.as_view()),
    path('rv/<int:pk>/update', views.RvUpdateView.as_view()),
    path('new/', views.RvCreateView.as_view()),
    path('rv/<int:pk>/delete', views.RvDeleteView.as_view()),
    path('rent/', views.RentListView.as_view()),
    path('rent/new/', views.RentCreateView.as_view()),
]

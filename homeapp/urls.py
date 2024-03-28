from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_review/', views.add_review, name='add_review'),
    path('review_success/', views.review_success, name='testimonial'),
    path('reg/', RegView.as_view(), name='reg'),
    path('logout/', logout_user, name='logout'),
    path('accounts/profile/', LoginView.as_view(), name='login'),
    path('food/<int:pk>/', DetailView.as_view(), name='food_slug'),
]

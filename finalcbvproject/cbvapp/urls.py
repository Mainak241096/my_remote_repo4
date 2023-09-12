from django.urls import path
from cbvapp import views

urlpatterns = [
    path('drinks/',views.DrinkListView.as_view(),name='list'),
    path('create/',views.DrinksCreateView.as_view()),
    path('detail/<int:pk>',views.DrinksDetailView.as_view()),
    path('update/<int:pk>',views.DrinksUpdateView.as_view()),
    path('delete/<int:pk>',views.DrinksDeleteView.as_view()),
]

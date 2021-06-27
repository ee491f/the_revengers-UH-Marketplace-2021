from django.urls import path
from . import views

app_name = 'uhmarketplace' # allows using 'uhmarketplace:index' for url and reverse_lazy methods
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='createtextbook'),
    path('updatetextbook/<int:pk>', views.UpdateView.as_view(), name='updatetextbook'),
    path('deletetextbook/<int:pk>', views.DeleteView.as_view(), name='deletetextbook'),
    path('textbook/', views.TextbookView.as_view(), name='textbook'),
    path('dorm/', views.DormView.as_view(), name='dorm'),
    path('classes/', views.ClassesView.as_view(), name='classes'),
    path('foodie/', views.FoodieView.as_view(), name='foodie'),
    path('supplies/', views.SuppliesView.as_view(), name='supplies'),
    path('orderDate/', views.OrderDateView.as_view(), name='orderDate'),

]

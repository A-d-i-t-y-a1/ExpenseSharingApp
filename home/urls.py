from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.addExpense, name='addExpense'),
    path('checkDue/', views.checkDue, name='checkDue'),
]

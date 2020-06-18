from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='expenses'),
    path('add-expenses',views.add_expense, name='add_expenses')
]
from django.urls import path
from lecture1 import views
urlpatterns=[
    path('',views.hello),
    path('db_values',views.db_values),
]
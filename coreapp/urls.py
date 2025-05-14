from django.urls import path, include
from coreapp.views import *
urlpatterns = [
    path('',home_view,name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', loginview, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('question/', question_view, name='question'),
    path('logout/', logout_view, name='logout'),
    path('export_excel/', export_excel, name='export_excel'),
]
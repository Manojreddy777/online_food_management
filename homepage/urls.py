from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404

from .views import custom_404_view

urlpatterns = [

    path("", views.index, name="login"),
    path('loggedin/', views.loggedIn, name="loggedin" ),
    path('logout/', views.logoutUser, name="logout" ),
    path('register/', views.registerUser, name="register" ),
    path('error-test/', views.error_test_view, name='error_test'),
    path('debug_test_view/', views.debug_test_view, name='debug_test_view'),
    path('test_logging/', views.test_logging, name='test_logging'),

    # path('feedback/', views.feedback, name="feedback" )

]
handler404 = custom_404_view  # Set the custom handler here

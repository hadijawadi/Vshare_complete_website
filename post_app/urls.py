from django.urls import path
from . import views


app_name =  'post_app'
urlpatterns = [
    path('',views.home_post, name='home_post'),
    path('text',views.create_text_post, name='create_text_post'),
]
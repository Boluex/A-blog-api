from django.urls import path
from.import views
from users import views as user_views
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken import views as auth_views
urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('register/',user_views.sign_up,name='register'),
    path('login/',auth_views.obtain_auth_token,name='login'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('comment/<int:id>',views.reply,name='comment'),
    path('update/<int:id>',views.update,name='update'),
    path('u_comment/<int:id>',views.update_comment,name='update_comment'),
    path('d_comment/<int:id>',views.delete_comment,name='delete_comment'),
    path('dt_comment/<int:id>',views.detail_comment,name='detail_comment'),
]
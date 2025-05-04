from django.urls import path
from . import views

urlpatterns = [
    path('testing/',views.testing,name="test"),
    path('',views.signup,name="Signup"),
    path('login/',views.login_view,name='login'),
    path('dummy/',views.create_dummy,name="dummy"),
    path('testing/',views.testing,name="testing"),
    path('tes/',views.tes,name='tes'),
    path('load_detail/',views.load_user_details,name='load_user_details'),

   
    path('edit/<str:blog_id>/', views.edit, name='edit_document'),
    path('update/<str:document_id>/', views.update_data, name='update_data'),
    path('delete/<str:blog_id>/', views.delete_data, name='delete_data'),
]  
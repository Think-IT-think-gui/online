from django.urls import path
from . views import Login_Api,Signup_Api,Cart_Api,Product_Api,Admin_Api,Message_Api,Home,Profile_Api,Categories_Api,Home_2,Request_Product,Rem_Cart,Account_Status,Logout,About,All,Remove_Product,Search_Api,Set_user,Set_basic,Set_pass,New_password,Set_Image,Delete_account,Validate_action,Pay,Log_out,Home_content
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login', Login_Api.as_view(), name="login" ),
    path('signup', Signup_Api.as_view()),
    path('cart/<str:pk>', Cart_Api.as_view()),
    path('about/<str:pk>', About.as_view()),
    path('log/<str:pk>', Account_Status.as_view()),
    #path('logout', Logout.as_view()),
    path('product/<str:pk>', Product_Api.as_view()),
    path('delete_cart', Rem_Cart.as_view()),
    path('sudo_admin', Admin_Api.as_view()),
    path('message/<str:pk>', Message_Api.as_view()),
    path('', Home.as_view(),name="defult"),
    path('get_more', All.as_view()),
    path('categories/<str:pk>', Categories_Api.as_view()),
    path('home/<str:pk>', Home_2.as_view(),),
    path('requested_product/<str:pk>/<str:pk2>', Request_Product.as_view()),
    path('profile', Profile_Api.as_view(), name="profile"),
    path('Rem_pro', Remove_Product.as_view(), name="profile"),
     path('Find/<str:pk1>/<str:pk2>', Search_Api.as_view()),
    path('set_up/<str:pk>', Set_user.as_view()),
    path('edit_basic/<str:pk>', Set_basic.as_view()),
    path('Set_pass/<str:pk>', Set_pass.as_view()),
    path('New_password', New_password.as_view()),
    path('Set_Image/<str:pk>', Set_Image.as_view()),
    path('Delete_account', Delete_account.as_view()),
    path('Validate_action/<str:pk>', Validate_action.as_view()),
    path('pay', Pay.as_view()),
    path('content/<str:pk>', Home_content.as_view()),
    path('log_out/<str:pk>', Log_out.as_view()),










]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'), 
    path('loginandregister/',views.loginandregister,name='loginandregister'),   
    path('handlesignup/',views.handlesignup,name='handlesignup'),
    path('handlelogin/',views.handlelogin,name='handlelogin'),
    path('handlelogout/',views.handlelogout,name='handlelogout'),
    # path('recommended/',views.recommended,name='recommended'),
    path('updateprofileform/',views.updateprofileform,name="updateprofileform"),
    path('updateprofile/',views.updateprofile,name="update"),
    path('updatepasswordform/',views.updatepasswordform,name="updatepasswordform"),
    path('updatepassword/',views.updatepassword,name="updatepassword"),
    path('foryou/',views.foryou,name='foryou'),
    path('fullmenu/',views.fullmenu,name='fullmenu'),
    path('viewfood/<int:id1>',views.viewfood,name="viewfood"),
    path('viewSpecialfood/<int:id1>',views.viewSpecialfood,name="viewSpecialfood"),
    path('cart/',views.cart,name="cart"),
    path('updatecart/<int:id2>',views.updatecart,name="updatecart"),
    path('removefromcart/<int:id3>',views.removefromcart,name="removefromcart"),
    path('checkout/',views.checkout,name="checkout"),
    path('confirmorder/',views.confirmorder,name="confirmorder"),
    path('cancelorder/<int:id>',views.cancelorder,name="cancelorder"),
    path('ordertracker/',views.ordertracker,name="ordertracker"),
    path('reviews/',views.reviews,name='reviews'),
    path('removereview/<int:id>',views.removereview,name='removereview'),
    path('confirmEpay/',views.confirmEpay,name='confirmEpay'),
    path('esewaRequest/<int:order_id>',views.esewaRequest,name='esewaRequest'),
]

#for loading the static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
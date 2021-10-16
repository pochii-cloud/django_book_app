from django.urls import path, include
from . import views
from django.conf.urls import url, include
from bapp.views import *

appname = 'bapp'

urlpatterns = [

    path('', views.dash, name='homeview'),

    # Purchase Service
    # path('addbook', views.addbook, name='addbook'),
    # path('planselection', views.planselection, name='planselection'),
    # path('planconfirmation', views.planconfirmation, name='planconfirmation'),
    # path('orderconfirmation', views.orderconfirmation, name='orderconfirmation'),

    # cancel order - order will be marked as cancelled and refund request will be initiated
    path('cancel_activeorder', views.cancel_activeorder, name='cancel_activeorder'),
    path('refund', views.refund, name='refund'),
    path('refund_confirmation', views.refund_confirmation, name='refund_confirmation'),

    # General
    path('orderhistory', views.orderhistory, name='orderhistory'),
    path('vieworder', views.vieworder, name='vieworder'),
    path('cancel', views.cancelorder, name='cancel'),

    # bookview
    path('booklist', views.booklist, name='booklist'),
    path('viewbook/<slug:slug>/', views.viewbook, name='viewbook'),
    # to add general details of a book
    path('addbook/', views.addbook, name='addbook'),
    path('addchapter/<slug:slug>/', views.addchapter, name='addchapter'),
    path('editbook/<slug:slug>/', views.editbook, name='editbook'),
    path('changeorder/', views.changeorder, name='changeorder'),
    # to drag and drop files
    path('upload/', views.file_upload_view, name='upload-view'),
    # services
    path('myservices', views.myservices, name='myservices'),
    path('servicelist', views.servicelist, name='servicelist'),
    path('services/<slug:slug>/', views.viewservice, name='viewservice'),
    path('serviceconfirmation/', views.serviceconfirmation, name='serviceconfirmation'),
    path('serviceordersuccess/', views.serviceordersuccess, name='serviceordersuccess'),

    # admin

    # login

    path('login/', views.login_view, name='login'),
    path('auth/', views.log_usr, name='auth'),
    path('logout/', views.logoutUser, name="logout"),

]

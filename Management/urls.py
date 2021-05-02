from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path('register/',views.register, name='register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path("Dashboard_Customer/", views.Dashboard_customer, name="Dashboard_customer"),
    path("Dashboard_Staff/", views.Dashboard_Staff, name="Dashboard_Staff"),
    path("AboutUs/", views.AboutUs, name="AboutUs"),
    path("Dashboard_Staff/ManagementServices/", views.MS, name="MS"),
    path("Dashboard_Staff/Orders/", views.show_order, name="order"),
    path("Dashboard_Staff/ManagementServices/team",views.team,name="team"),
    path("Dashboard_Staff/Orders/<str:id>", views.check_order, name="check_order"),
    path("Dashboard_Staff/Orders/Done/<str:id>",views.DeliveryDone,name="DeliveryDone"),
    path("Dashboard_Staff/ManagementServices/team/<str:user_name>",views.fire,name="fire"),
    # path("Dashboard_Staff/transaction",views.makeTransc,name="transc"),
    # url(r'^export-exl/$', views.export, name='export'),
    # url(r'^export-csv/$', views.export, name='export'),
]
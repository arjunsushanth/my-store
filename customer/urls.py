from django.urls import path
from customer import views

urlpatterns=[
    path("register",views.SignUpView.as_view(),name="register"),
    path("",views.SigninView.as_view(),name="signin"),
    path("customer/home",views.HomeView.as_view(),name="user-home"),
    path("product/details/<int:id>",views.ProductDetailView.as_view(),name="product-details"),
    path("product/carts/<int:id>/add",views.addto_cart,name="addto-cart"),
    path("carts/all",views.CartListView.as_view(),name="cart-list"),
    path("order/add/<int:cid>/<int:pid>",views.OrderView.as_view(),name="place-order"),
    path("order/all",views.MyOrdersView.as_view(),name="my-orders"),
    path("orders/<int:id>/remove",views.Cancelorder_view,name="order-cancel"),
    path("customer/accounts/signout",views.logout_view,name="signout")



]
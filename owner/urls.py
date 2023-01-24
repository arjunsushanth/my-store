from django.urls import path
from owner import views

urlpatterns = [
    path("register",views.SignUpView.as_view()),
    path("home",views.HomeView.as_view()),
    path("login",views.SigninView.as_view()),
    path("product/add",views.ProductCreateView.as_view())
    ]
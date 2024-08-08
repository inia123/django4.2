from django.urls import path

from pjuser.views import RegisterView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='pjlogin'),
    path('register/', RegisterView.as_view(), name='pjregister'),
]

from django.urls import path
from .views import signup, user_login, classroom


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', user_login, name="user_login"),
    path('classroom/', classroom, name="crud_classroom")
    
    
]


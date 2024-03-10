from django.urls import path
from .views import signup, user_login, classroom, user_logout, add_classroom, update_classroom, delete_classroom



urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('classroom/', classroom, name="crud_classroom"),
    path("update-classroom/<int:id>/", update_classroom, name="update_classroom"),
    path("delete-classroom/<int:id>/", delete_classroom, name="delete_classroom"),
    path("add-classroom/", add_classroom, name="add_classroom"),

    
]


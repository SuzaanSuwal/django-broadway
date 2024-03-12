from django.urls import path
from .views import signup, user_login, classroom, user_logout, add_classroom, crud_student, update_classroom, delete_classroom, user_profile, update_profile, add_student



urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('classroom/', classroom, name="crud_classroom"),
    path("update-classroom/<int:id>/", update_classroom, name="update_classroom"),
    path("delete-classroom/<int:id>/", delete_classroom, name="delete_classroom"),
    path('student/', crud_student, name="crud_student"),
    path("add-classroom/", add_classroom, name="add_classroom"),
    path("add-student/", add_student, name="add_student"),
    path("profile/", user_profile, name="user_profile"),
    path("update-profile/", update_profile, name="update_profile")
    

    
]


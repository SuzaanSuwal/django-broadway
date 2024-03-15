from django.urls import path
from .views import PortfolioView, ClassRoomView, ClassRoomCreateView, UpdateClassRoomView, DeleteClassRoomView, \
    UserProfileView



urlpatterns = [
    path('portfolio/', PortfolioView.as_view(), name="classbased_portfolio"),
    path("classroom/", ClassRoomView.as_view(), name="classbased_classroom"),
    path("add-classroom/", ClassRoomCreateView.as_view(), name="classbased_add_classroom"),
    path("update-classroom/<int:pk>/", UpdateClassRoomView.as_view(), name="cb_update_classroom"),
    path("delete-classroom/<int:pk>/", DeleteClassRoomView.as_view(), name="cb_delete_classroom"),
    path("user-profile/<int:pk>/", UserProfileView.as_view(), name="cb_user_profile"),
    
]
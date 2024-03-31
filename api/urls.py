from django.urls import path
from .views import home, HomeView, StudentAPIView, StudentListAPIView, SimpleClassRoomView, SimpleClassRoomListView, \
    ClassRoomRetrieveView, ClassRoomView, ClassRoomUpdateDeleteView
    
from .generic_views import ClassRoomGenericView, ClassRoomGenericCreateView, ClassRoomListCreateView, ClassRoomUpdateView,\
    CLassRoomViewSet, ClassRoomRUDView, UserProfileViewSet, UserViewSet

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('classroom-viewset', CLassRoomViewSet, basename="classroom")
router.register('profile-viewset', UserProfileViewSet, basename="Userprofile")
router.register('user-viewset', UserViewSet, basename="User")
# router.register('student-viewset', StudentViewSet)




urlpatterns = [
    path("home/", home),
    path("cb-apiview/", HomeView.as_view()),
    path("student-apiview/", StudentAPIView.as_view()),
    path("student-list-apiview/", StudentListAPIView.as_view()),
    path("simple-classroom/", SimpleClassRoomView.as_view()),
    path("simple-classroom-list/", SimpleClassRoomListView.as_view()),
    
    path("classroom/<int:id>/", ClassRoomRetrieveView.as_view()),
    path("classroom-update-delete/<int:id>/", ClassRoomUpdateDeleteView.as_view()),
    path("classroom/", ClassRoomView.as_view()),
 
 
    # Login URL
    path('login/', obtain_auth_token)
 
    
]


generic_urlpatterns = [
    path("generic-classroom/", ClassRoomGenericView.as_view()),
    path("generic-classroom-create/", ClassRoomGenericCreateView.as_view()),
    path("generic-classroom-list-create/", ClassRoomListCreateView.as_view()),
    path("generic-classroom-update/<int:pk>/", ClassRoomUpdateView.as_view()),
    path("generic-classroom-rud/<int:pk>/", ClassRoomRUDView.as_view()),  # rud => Retrieve Update Delete



]

urlpatterns += generic_urlpatterns + router.urls
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('student/', views.StudentView.as_view(), name="student-dashboard"),
    path('api/accounts/', include('rest_auth.urls')),
    path('api/accounts/registration/', include('rest_auth.registration.urls')), 
    path('api/accounts/<int:pk>/', views.UserUpdateAPIView.as_view(), name="user_update"),
    path('logout/',views.UserLogoutView.as_view(), name="logout"),
    path('api/clearance/create/', views.ClearanceCreateAPIView.as_view(), name="create_row"),
    path('api/clearance/<int:pk>/', views.ClearanceRequestAPIView.as_view(), name="update_request"),
]

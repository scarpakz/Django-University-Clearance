from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import views 
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import UserProfile
from form.models import Clearance, ClearanceStatus
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .serializers import UserSerializer, ClearanceRequestSerializer, ClearanceAddRowSerializer
from rest_framework import generics
from .forms import UserForm, SignUpForm

class LoginView(ListView):
    model = UserProfile
    template_name = 'account/login.html'

@method_decorator(login_required, name="dispatch")
class StudentView(TemplateView):
    template_name = 'account/student.html'

class UserLogoutView(views.LogoutView):
    model = User
    template_name = 'account/logout.html'

class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClearanceCreateAPIView(generics.CreateAPIView):
    queryset = Clearance.objects.all()
    serializer_class = ClearanceAddRowSerializer

class ClearanceRequestAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clearance.objects.all()
    serializer_class = ClearanceRequestSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import TemporaryPassword, Media
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from faker import Faker
import random
import string
import datetime
from rest_framework import permissions, viewsets
from firstapp.serializers import GroupSerializer, UserSerializer




fake = Faker()

random_name = fake.name()


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def initialize(request):
    if request.method == 'GET':
        username = random_name
        password = generate_password()
        user = User.objects.create_user(username=username, password=password)
        user.save()
        preface = TemporaryPassword(user=user, temporary_password=password, created_at=datetime.datetime.now())
        preface.save()


@login_required
def home(request):
    context = {
        'success': 'success'
    }
    return render(request, 'home.html', context)


def login_user(request):
    suite = Media.objects.get(name='suite logo')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'image': suite})


class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    """
    Api Endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

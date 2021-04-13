from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import User
from addantique.models import Addantique
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )



        return redirect('login')



class Home(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def get(self, request):
        antique = Addantique.objects.all()
        return render(request, 'home.html', {'antique' : antique})


class Details(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def get(self, request, pk):
        antique = Addantique.objects.get(id=pk)
        return render(request, 'details.html', {'antique' : antique})



def logout_user(request):
    logout(request)
    return redirect('login')


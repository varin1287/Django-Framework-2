from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from basketapp.models import Basket
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {'form': form, 'head': 'авторизация'}
    return render(request, 'authapp/login.html', context)

class UserCreateView(CreateView):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:login')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

class UserProfileView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    # login_url = 'main:products'
    # success_url = reverse_lazy('main:index')

    def get_success_url(self):
        self.success_url = reverse_lazy('auth:profile', args=[self.kwargs['pk']])
        return str(self.success_url)



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('auth:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {'head': 'GeekShop - Профиль',
#                'form': form,
#                'baskets': Basket.objects.filter(user=request.user),
#                }
#     return render(request, 'authapp/profile.html', context)



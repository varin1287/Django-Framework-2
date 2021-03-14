from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from mainapp.models import Product
from adminapp.forms import AdminUserRegisterForm, AdminUserProfileForm, AdminProductsRegisterForm, AdminProductsProfileForm

@user_passes_test(lambda u: u.is_superuser, login_url='mainapp:products')
def index(request):
    return render(request, 'adminapp/index.html', {'title' : 'Админ'})

# Пользователи

class UserListView(ListView):
    model = User
    template_name = 'adminapp/admins_user_read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context



# @user_passes_test(lambda u: u.is_superuser)
# def admins_user_read(request):
#     context = {'users': User.objects.all()}
#     return render(request, 'adminapp/admins_user_read.html', context)

class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = AdminUserRegisterForm
    success_url = reverse_lazy('admins:admins_user_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Новый пользователь'
        return context

#
# @user_passes_test(lambda u: u.is_superuser)
# def admins_user_create(request):
#     if request.method == 'POST':
#         form = AdminUserRegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admins_user_read'))
#     else:
#         form = AdminUserRegisterForm()
#     context = {'form': form, }
#     return render(request, 'adminapp/admin-users-create.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin_user_update_delete.html'
    form_class = AdminUserProfileForm
    success_url = reverse_lazy('admins:admins_user_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def admins_user_update(request, id=None):
#     user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = AdminUserProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admins_user_read'))
#     else:
#         form = AdminUserProfileForm(instance=user)
#     context = {'current_user': user,
#                'form': form,
#                }
#     return render(request, 'adminapp/admin_user_update_delete.html', context)

class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin_user_update_delete.html'
    success_url = reverse_lazy('admins:admins_user_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



# @user_passes_test(lambda u: u.is_superuser)
# def admins_user_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admins_user_read'))

# Продукты

class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/admin_products_read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Продукты'
        return context


class ProductsCreateView(CreateView):
    model = Product
    template_name = 'adminapp/admin_products_create.html'
    form_class = AdminProductsRegisterForm
    success_url = reverse_lazy('admins:admin_products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавить продукт'
        return context


class ProductsUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/admins_products_update_delete.html'
    form_class = AdminProductsProfileForm
    success_url = reverse_lazy('admins:admin_products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование продукта'
        return context

class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/admins_products_update_delete.html'
    success_url = reverse_lazy('admins:admin_products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsDeleteView, self).dispatch(request, *args, **kwargs)



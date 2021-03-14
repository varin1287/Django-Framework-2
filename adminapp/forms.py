from authapp.forms import UserRegisterForm, UserProfileForm
from django import forms
from mainapp.models import Product

class AdminUserRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(AdminUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class AdminUserProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(AdminUserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False




class AdminProductsRegisterForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(AdminProductsRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['image'].widget.attrs['placeholder'] = 'Загрузите изображение продукта'
        self.fields['description'].widget.attrs['placeholder'] = 'Полное описание продукта'
        self.fields['short_description'].widget.attrs['placeholder'] = 'Краткое описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите цену'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Укажите кол-во'
        self.fields['category'].widget.attrs['placeholder'] = 'Укажите категорию продукта'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class AdminProductsProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(AdminProductsProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['image'].widget.attrs['placeholder'] = 'Загрузите изображение продукта'
        self.fields['description'].widget.attrs['placeholder'] = 'Полное описание продукта'
        self.fields['short_description'].widget.attrs['placeholder'] = 'Краткое описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите цену'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Укажите кол-во'
        self.fields['category'].widget.attrs['placeholder'] = 'Укажите категорию продукта'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'




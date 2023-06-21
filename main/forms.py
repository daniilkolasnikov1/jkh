from .models import House, Tenant, Payment
from django.forms import ModelForm, TextInput, NumberInput, CharField, PasswordInput, DateInput, Select
from django.contrib.auth.forms import AuthenticationForm


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ['floors', 'apartments', 'address', 'year_built']
        labels = {
            'floors': 'Этажи',
            'apartments': 'Кол-во апартаментов',
            'address': 'Адрес',
            'year_built': 'Год постройки',
        }
        widgets = {
            'floors': NumberInput(attrs={'class': 'form-control mb-3'}),
            'apartments': NumberInput(attrs={'class': 'form-control mb-3'}),
            'address': TextInput(attrs={'class': 'form-control mb-3'}),
            'year_built': NumberInput(attrs={'class': 'form-control mb-3'}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = CharField(
        label='Имя пользователя',
        widget=TextInput(attrs={'class': 'form-control'})
    )
    password = CharField(
        label='Пароль',
        widget=PasswordInput(attrs={'class': 'form-control'})
    )


class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'date_of_birth', 'phone', 'email', 'house']
        labels = {
            'name': 'ФИО',
            'date_of_birth': 'Дата рождения',
            'phone': 'Телефона',
            'email': 'Почта',
            'house': 'Дом',
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-3'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'phone': TextInput(attrs={'class': 'form-control mb-3'}),
            'email': TextInput(attrs={'class': 'form-control mb-3'}),
            'house': Select(attrs={'class': 'form-control mb-3'}),
        }


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['date', 'sum', 'address', 'tenant']
        labels = {
            'date': 'Дата',
            'sum': 'Сумма',
            'address': 'Адрес',
            'tenant': 'Жилец',
        }
        widgets = {
            'date': DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'sum': NumberInput(attrs={'class': 'form-control mb-3'}),
            'address': Select(attrs={'class': 'form-control mb-3'}),
            'tenant': Select(attrs={'class': 'form-control mb-3'}),
        }


from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import logout
from django.views.generic import ListView
from .models import House, Tenant, Payment
from .forms import HouseForm, TenantForm, PaymentForm
from django.contrib.auth import views as auth_views
import stripe


def index(request):
    data = {
        'title': 'Главная страница'
     }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def konatky(request):
    return render(request, 'main/konatky.html')


class HouseListView(ListView):
    model = House
    context_object_name = 'houses'
    template_name = 'houses/list.html'
    ordering = ['floors']  # default ordering

    def get_ordering(self):
        ordering = self.request.GET.get('sort', self.ordering)
        return ordering

    def get_queryset(self):
        queryset = super().get_queryset()
        floors_filter = self.request.GET.get('floors')
        apartments_filter = self.request.GET.get('apartments')
        address_filter = self.request.GET.get('address')
        year_built_filter = self.request.GET.get('year_built')
        if floors_filter:
            queryset = queryset.filter(floors=floors_filter)
        if apartments_filter:
            queryset = queryset.filter(apartments=apartments_filter)
        if address_filter:
            queryset = queryset.filter(address__icontains=address_filter)
        if year_built_filter:
            queryset = queryset.filter(year_built=year_built_filter)
        return queryset


def new_house(request):
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('house_list')
    else:
        form = HouseForm()
    return render(request, 'houses/create_form.html', {'form': form})


def edit_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == "POST":
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house_list')
    else:
        form = HouseForm(instance=house)
    return render(request, 'houses/create_form.html', {'form': form})


class CustomLoginView(auth_views.LoginView):
    def get_success_url(self):
        # url = super().get_success_url()
        url = "/"
        return url


class TenantListView(ListView):
    model = Tenant
    context_object_name = 'tenants'
    template_name = 'tenants/list.html'
    ordering = ['name']  # default ordering

    def get_ordering(self):
        ordering = self.request.GET.get('sort', self.ordering)
        return ordering

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get('name')
        date_filter = self.request.GET.get('date')
        phone_filter = self.request.GET.get('phone')
        email_filter = self.request.GET.get('email')
        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        if date_filter:
            queryset = queryset.filter(date_of_birth=date_filter)
        if phone_filter:
            queryset = queryset.filter(phone__icontains=phone_filter)
        if email_filter:
            queryset = queryset.filter(email__icontains=email_filter)
        return queryset


def new_tenant(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    return render(request, 'tenants/create_form.html', {'form': form})


def edit_tenant(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    if request.method == "POST":
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenants/create_form.html', {'form': form})


class PaymentListView(ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'payments/list.html'
    ordering = ['date']  # default ordering

    def get_ordering(self):
        ordering = self.request.GET.get('sort', self.ordering)
        return ordering

    def get_queryset(self):
        queryset = super().get_queryset()
        date_filter = self.request.GET.get('date')
        sum_filter = self.request.GET.get('sum')
        address_filter = self.request.GET.get('address')
        if date_filter:
            queryset = queryset.filter(date=date_filter)
        if sum_filter:
            queryset = queryset.filter(sum=float(sum_filter))
        if address_filter:
            try: 
                addressFilter = House.objects.filter(address = address_filter ).get()
            except Exception as e:
                addressFilter = ""

            print(addressFilter)
            if addressFilter != "":
                queryset = queryset.filter(address=addressFilter)
        return queryset


def new_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payments/create_form.html', {'form': form})


def edit_payment(request, pk):
    payment = Payment.objects.get(pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payments/create_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')



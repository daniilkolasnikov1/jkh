from django.urls import path
from . import views
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('kontaky', views.konatky, name='konatky'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.CustomLoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('houses/', views.HouseListView.as_view(), name='house_list'),
    path('houses/new', views.new_house, name='new_house'),
    path('houses/<int:pk>/edit/', views.edit_house, name='edit_house'),
    path('tenants/', views.TenantListView.as_view(), name='tenant_list'),
    path('tenants/new', views.new_tenant, name='new_tenant'),
    path('tenants/<int:pk>/edit/', views.edit_tenant, name='edit_tenant'),
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/new', views.new_payment, name='new_payment'),
    path('payments/<int:pk>/edit/', views.edit_payment, name='edit_payment'),
]

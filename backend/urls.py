from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from backend.views import PartnerUpdate, \
    RegisterAccount, LoginAccount, CategoryView, \
    ShopView, ProductInfoView, BasketView, AccountDetails, \
    ContactView, OrderView, PartnerState, PartnerOrders, \
    ConfirmAccount, RegistrationView

from backend.views import RestrictedApiView, RegistrationView, ContactView, index
# https://djoser.readthedocs.io/en/latest/base_endpoints.html

app_name = 'backend'
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('rest_framework.urls')),
    path('user/details/', AccountDetails.as_view(), name='user-details'),
    path('password_reset/', reset_password_request_token, name='password-reset'),
    path('password_reset/confirm/', reset_password_confirm, name='password-reset-confirm'),
    path('contact/', ContactView.as_view()),

    path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state/', PartnerState.as_view(), name='partner-state'),
    path('partner/orders/', PartnerOrders.as_view(), name='partner-orders'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('shops/', ShopView.as_view(), name='shops'),
    path('products/', ProductInfoView.as_view(), name='shops'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('order/', OrderView.as_view(), name='order'),
]

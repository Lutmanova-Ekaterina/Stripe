from django.urls import path, include

from subscribe.apps import SubscribeConfig
from subscribe.views import CreateCheckoutSessionView, SubscribeLandingPageView, SuccessView, CancelView

app_name = SubscribeConfig.name

urlpatterns = [
    path('landing-page/', SubscribeLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]


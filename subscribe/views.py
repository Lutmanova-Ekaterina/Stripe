
import stripe
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from subscribe.models import Subscribe

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'subscribe/success.html'


class CancelView(TemplateView):
    template_name = 'subscribe/cancel.html'


class SubscribeLandingPageView(TemplateView):
    template_name = "subscribe/landing.html"

    def get_context_data(self, **kwargs):
        subscribe = Subscribe.objects.get(name="Test subscribe")
        context = super(SubscribeLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "subscribe": subscribe,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        subscribe_id = self.kwargs["pk"]
        subscribe = Subscribe.objects.get(id=subscribe_id)
        print(subscribe)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': subscribe.price,
                        'product_data': {
                            'name': subscribe.name,
                            # 'images': [],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})

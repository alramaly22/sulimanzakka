from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import stripe

# إعداد مفتاح API الخاص بـ Stripe من الإعدادات
stripe.api_key = settings.STRIPE_API_KEY

YOUR_DOMAIN = "https://testsulieman.vercel.app"

def index(request):
    return render(request, 'accounts/index.html')

def about(request):
    return render(request, 'accounts/about.html')

def calc(request):
    return render(request, 'accounts/calc.html')

def calc2(request):
    return render(request, 'accounts/calc2.html')

def create_checkout_session(request):
    if request.method == 'POST':
        price_id = request.POST.get('price_id')
        print("✅ Request received with price_id:", price_id)

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode='payment',
                success_url=YOUR_DOMAIN + '/second/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            return redirect(checkout_session.url, code=303)

        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return HttpResponse(f"Stripe Error: {str(e)}")

    return HttpResponse("Invalid request", status=400)


def success(request):
    return render(request, 'accounts/success.html')

def cancel(request):
    return render(request, 'accounts/cancel.html') 

def second(request):
    return render(request, 'accounts/second.html')

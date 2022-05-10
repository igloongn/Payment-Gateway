from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Payment
from .forms import PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    messages.error(request, "Message sent." )
    return render(request, "index.html", {})


# @login_required
def initiate_payment(request):
    p = {}
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            p["payment"] = payment
            p["amount"] = payment.amount_value()
            p["msg"] = "This is from initiate payment"
            p["paystack_public_key"] = settings.PAYSTACK_PUBLIC
            return render(request, "make_payment.html", p)
    else:
        payment_form = PaymentForm()
        p["payment_form"] = payment_form
        return render(request, "initiate_payment.html", p)


def verify_payment(request, ref):
    p = {}
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Your payment has been verified")
        # return HTTPResponse('Your payment has been verified')
    else:
        messages.error(request, "Failed Payment")
        # return HTTPResponse('Failed Payment')
    return redirect("initiate")


# This is Strictly for React payment
# React Payment
from django.http import JsonResponse
def getSecretKey(request):
    testSecretKey = settings.PAYSTACK_PUBLIC
    return JsonResponse({'key': testSecretKey })
    

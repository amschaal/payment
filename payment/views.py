from django.shortcuts import render, redirect
from payment.forms import CreatePaymentForm, ModifyPaymentForm
from payment.models import Payment
from django.contrib.auth.decorators import user_passes_test
from touchnet.forms import TouchnetPostForm

def index(request):
    return render(request, 'payment/index.html', {})

@user_passes_test(lambda u: u.is_staff)
def create_payment(request):
    if request.method == 'GET':
        form = CreatePaymentForm()
    elif request.method == 'POST':
        form = CreatePaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect('payment', id=payment.id)
    return render(request, 'payment/create_payment.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def modify_payment(request, id):
    payment = Payment.objects.get(id=id)
    if payment.is_paid:
        return render(request, 'payment/modify_payment.html', {'payment': payment})
    if request.method == 'GET':
        form = ModifyPaymentForm(instance=payment)
    elif request.method == 'POST':
        form = ModifyPaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save()
            return redirect('payment', id=payment.id)
    return render(request, 'payment/modify_payment.html', {'form': form, 'payment': payment})

@user_passes_test(lambda u: u.is_staff)
def payments(request):
    payments = Payment.objects.all().order_by('-created')
    return render(request, 'payment/payments.html', {'payments': payments})

# @user_passes_test(lambda u: u.is_staff)
def payment(request, id):
    payment = Payment.objects.get(id=id)
    return render(request, 'payment/payment.html', {'payment': payment})

def pay(request, id):
    payment = Payment.objects.get(id=id)
    form = TouchnetPostForm(payment=payment)
    return render(request, 'payment/pay.html', {'payment': payment, 'form': form})
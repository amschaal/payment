from django import forms
from payment.models import Payment

class CreatePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('account','amount','order_id','description')

class ModifyPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('account','amount','order_id','description','disabled')
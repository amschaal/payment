from django import forms
from payment.models import Payment

class CreatePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('account','amount','description')

class ModifyPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('account','amount','description','disabled')
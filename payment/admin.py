from django.contrib import admin
from payment.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    exclude = ('status',)

admin.site.register(Payment, PaymentAdmin)
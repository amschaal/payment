from django.contrib import admin
from payment.models import Payment, Account

class PaymentAdmin(admin.ModelAdmin):
    exclude = ('status',)
class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Account, AccountAdmin)
from django.db import models
import uuid

class Payment(models.Model):
    TYPE_GENERIC = 'GENERIC'
    STATUS_UNPAID = 'UNPAID'
    STATUS_PAID = 'PAID'
    STATUS_PENDING = 'PENDING'
    STATUS_INVALID_AMOUNT = 'INVALID_AMOUNT'
#     STATUS_CANCELLED = 'CANCELLED'
    STATUS_ERROR = 'ERROR'
    STATUS_CHOICES = ((STATUS_UNPAID, 'Unpaid'), (STATUS_PAID, 'Paid'), (STATUS_PENDING, 'Payment Pending'), (STATUS_INVALID_AMOUNT, 'Invalid Amount Paid'), (STATUS_ERROR, 'Processing Error'))
    TYPE_CHOICES = ((TYPE_GENERIC, TYPE_GENERIC),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_GENERIC)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_UNPAID)
    created = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True)
    external_id = models.CharField(max_length=100, null=True)
    
    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.type, self.id, self.amount)
from django.db import models
import uuid

class Account(models.Model):
    fid = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return '{0} - {1}'.format(self.fid, self.name)
    class Meta:
        ordering = ('fid', )
    
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
    account = models.ForeignKey(Account, related_name='payments')
#     chart_string = models.CharField(max_length=1, null=True)
#     fau = models.CharField
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_UNPAID)
    created = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True)
    transaction_id = models.CharField(max_length=100, null=True)
    disabled = models.BooleanField(default=False)
    @property
    def is_paid(self):
        return self.status == self.STATUS_PAID or self.transaction_id or self.paid_at
    def __unicode__(self):
        return '{0} - {1} - {2} ({3})'.format(self.type, self.id, self.amount, self.status)
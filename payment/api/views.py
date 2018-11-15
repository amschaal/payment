from rest_framework import viewsets
from payment.api.serializers import PaymentSerializer
from payment.models import Payment


class PaymentViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PaymentSerializer
    filter_fields = {'id':[ 'icontains'],'description':['icontains'],'status':['exact'],'disabled':['exact']}
#     search_fields = ('title',)
    ordering_fields = ('created','status','amount')
#     permission_classes = (EventPermission,)
    def get_queryset(self):
        return Payment.objects.all()
from rest_framework import viewsets
from payment.api.serializers import PaymentSerializer
from payment.models import Payment


class PaymentViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PaymentSerializer
    filter_fields = {'id':[ 'icontains'],'order_id':[ 'icontains'],'description':['icontains'],'status':['exact'],'disabled':['exact'],'created':['gte','lte'],'paid_at':['gte','lte'],'status':['exact']}
#     search_fields = ('title',)
    ordering_fields = ('created','status','amount','disabled','paid_at','order_id')
#     permission_classes = (EventPermission,)
    def get_queryset(self):
        return Payment.objects.all()
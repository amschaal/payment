from rest_framework import viewsets
from payment.api.serializers import PaymentSerializer
from payment.models import Payment
from rest_framework.decorators import list_route
from django.utils import timezone
from django.http.response import HttpResponse

class PaymentViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PaymentSerializer
    filter_fields = {'id':[ 'icontains'],'order_id':[ 'icontains'],'description':['icontains'],'status':['exact'],'disabled':['exact'],'created':['gte','lte'],'paid_at':['gte','lte'],'status':['exact']}
#     search_fields = ('title',)
    ordering_fields = ('created','status','amount','disabled','paid_at','order_id')
#     permission_classes = (EventPermission,)
    def get_queryset(self):
        return Payment.objects.all()
    @list_route()
    def export(self,request):
        import tablib
        payments = self.filter_queryset(self.get_queryset())
        fields = ['ID','Amount','Account FID', 'Account Name','Order ID', 'Description', 'Status','Created','Paid at','Transaction ID','Disabled']
        
        #add headers
        dataset = tablib.Dataset(headers=fields)
        #write data
        for p in payments:
            dataset.append([p.id,p.amount,p.account.fid,p.account.name,p.order_id,p.description,p.status,p.created.strftime("%Y-%m-%d %H:%M"),p.paid_at.strftime("%Y-%m-%d %H:%M") if p.paid_at else '',p.transaction_id,p.disabled])
        filetype = request.query_params.get('export_format','xls')
        filetype = filetype if filetype in ['xls','xlsx','csv','tsv','json'] else 'xls'
        content_types = {'xls':'application/vnd.ms-excel','tsv':'text/tsv','csv':'text/csv','json':'text/json','xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}
        response_kwargs = {
                'content_type': content_types[filetype]
            }
        filename = "payments_%s.%s"%(timezone.now().strftime("%Y_%m_%d__%H_%M"),filetype)
        response = HttpResponse(getattr(dataset, filetype), **response_kwargs)
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response
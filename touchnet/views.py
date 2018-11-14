from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
# from datetime import datetime
from touchnet.permissions import IPAddressPermission
# import logging
# from ezreg.payment.touchnet.processor import TouchnetPaymentProcessor
from payment.models import Payment
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny


"""
EXT_TRANS_ID    The departmental identifier passed in to the UPay site. (100)
UPAY_SITE_ID    (See above) (3)
POSTING_KEY    (See above) (variable)
PMT_STATUS    "success" upon a successful payment, "cancelled" if the user clicks the cancel button on the form. (20)
Variables sent only upon a successful payment:
PMT_AMT    The amount of the payment charged to the card. (numeric)
PMT_DATE    (today) (mm/dd/yyyy)
CARD_TYPE    The type of credit card used - spelled out (20)
TPG_TRANS_ID    The unique transaction ID assigned to the transaction by the payment gateway. (16)
NAME_ON_ACCT    Name of the card holder as shown on the card. (20)
ACCT_ADDR    Billing Address Street Address (40)
ACCT_CITY    Billing Address City Name (20)
ACCT_STATE    Billing Address State Code (2)
ACCT_ZIP    Billing Address Postal Code (20)
"""


@api_view(['POST'])
# @permission_classes([IPAddressPermission])
@permission_classes([AllowAny])
def postback(request):
    req = {k.upper():v for k,v in request.POST.items()} #Touchnet seems inconsistent about case
#     logger = logging.getLogger('touchnet')
    try:
        payment_id = req.get('EXT_TRANS_ID').split("PAYMENT_ID=").pop() #FID=12345;{FAU==12345;}PAYMENT_ID=XXXXXXXXXXX
        payment = Payment.objects.get(id=payment_id)
        posting_key = settings.TOUCHNET.get('POSTING_KEY')
        if posting_key != req.get('POSTING_KEY'):
            raise Exception("Invalid POSTING_KEY")
        if req.get('PMT_STATUS')=='success':
            payment.external_id = req.get('TPG_TRANS_ID')
            if float(req.get('PMT_AMT')) == float(payment.amount):
                payment.status = Payment.STATUS_PAID
                payment.paid_at = timezone.now()
                payment.save()
#                 email_status(payment)
            else:
                payment.status = Payment.STATUS_INVALID_AMOUNT
                payment.save()
#                 email_status(payment)
                raise Exception('Invalid amount posted %s, expecting %f' % (req.get('PMT_AMT'),payment.amount))
            payment.save()
#         elif req.get('PMT_STATUS')=='cancelled' and payment.status != Payment.STATUS_PAID:
#             payment.status = Payment.STATUS_CANCELLED
#             payment.save()
        return JsonResponse({'status':'ok','payment_status':payment.status})
    except Exception, e:
        # Get an instance of a logger
        payment.status = Payment.STATUS_ERROR
        payment.save()
#         logger.info("Error for EXT_TRANS_ID: %s"%req.get('EXT_TRANS_ID',''))
#         logger.error(e.message)
        return JsonResponse({'status':'error'},status=400)
        

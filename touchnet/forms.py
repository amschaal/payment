from django import forms
from django.conf import settings
from django.urls.base import reverse

# class TouchnetConfigurationForm(forms.Form):
#     FID = forms.CharField(max_length=5)
#     FAU = forms.CharField(max_length=30,required=False)
#     UPAY_SITE_ID = forms.IntegerField()
#     POSTING_KEY = forms.CharField(max_length=50)
#     UPAY_TEST_SITE_ID = forms.IntegerField()
#     TEST_POSTING_KEY = forms.CharField(max_length=50)

class TouchnetPostForm(forms.Form):
    UPAY_SITE_ID = forms.CharField(widget=forms.HiddenInput())
    EXT_TRANS_ID = forms.CharField(widget=forms.HiddenInput())
#     EXT_TRANS_ID_LABEL = forms.CharField(widget=forms.HiddenInput())
    SUCCESS_LINK = forms.URLField(required=False,widget=forms.HiddenInput())
    CANCEL_LINK = forms.URLField(required=False,widget=forms.HiddenInput())
    AMT = forms.CharField(widget=forms.HiddenInput)
    VALIDATION_KEY = forms.CharField(widget=forms.HiddenInput())
    EXT_TRANS_ID_LABEL = forms.CharField(widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        import base64
        import hashlib
        self.payment = kwargs.pop('payment')
        self.test = kwargs.pop('test', False)
        site = 'TEST' if self.test else 'PRODUCTION'
        conf = settings.TOUCHNET #settings.TOUCHNET_SITES['TEST'] if self.test else settings.TOUCHNET_SITES['PRODUCTION']
        if self.payment.account.fau:
            EXT_TRANS_ID = 'FID={};FAU={};PAYMENT_ID={}'.format(self.payment.account.fid,self.payment.account.fau,self.payment.id)#  if not conf.get('FAU') else 'FID=%s;FAU=%s;%s'%(conf['FID'],conf['FAU'],payment.registration.id), 
        else:
            EXT_TRANS_ID = 'FID={};PAYMENT_ID={}'.format(self.payment.account.fid,self.payment.id)
        if self.payment.invoice_id:
            EXT_TRANS_ID = 'INV={};'.format(self.payment.invoice_id) + EXT_TRANS_ID
        AMT = '{0:.2f}'.format(self.payment.amount)
        m = hashlib.md5()
        m.update(conf.get('POSTING_KEY')+EXT_TRANS_ID+AMT)
        data = {'UPAY_SITE_ID': conf.get('SITE_ID'),
                'EXT_TRANS_ID': EXT_TRANS_ID,
#                 'EXT_TRANS_ID_LABEL':payment.registration.event.title,
                'SUCCESS_LINK': settings.SITE_URL + reverse('payment',kwargs={'id':self.payment.id}),
                'CANCEL_LINK': settings.SITE_URL + reverse('pay',kwargs={'id':self.payment.id}),
                'AMT': AMT,
                'VALIDATION_KEY': base64.encodestring(m.digest()),
                'EXT_TRANS_ID_LABEL': 'Order ID {0}'.format(self.payment.order_id) if self.payment.order_id else self.payment.description 
                }
        print data
        m.update(conf.get('POSTING_KEY')+data['EXT_TRANS_ID']+str(data['AMT']))
#         data['VALIDATION_KEY']=base64.encodestring(m.digest())
#         form = TouchnetPostForm(initial=data)
        self.action = conf.get('URL')
        super(TouchnetPostForm, self).__init__(data, **kwargs)
    


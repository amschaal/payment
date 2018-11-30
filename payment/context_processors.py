from django.conf import settings
def site_settings(request):
    return {'site_settings':{'test':getattr(settings,'TEST',True)}}
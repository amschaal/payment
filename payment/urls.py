"""payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from payment import views
from touchnet.urls import urlpatterns as touchnet_urlpatterns
from rest_framework import routers
from payment.api.views import PaymentViewset

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewset, 'Payment')

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(touchnet_urlpatterns)),
    url(r'^api/', include(router.urls)),
    url(r'^payments/$', views.payments, name="payments"),
    url(r'^payments/create/$', views.create_payment, name="create_payment"),
    url(r'^payments/(?P<id>[0-9a-f-]+)/$', views.payment, name="payment"),
    url(r'^payments/(?P<id>[0-9a-f-]+)/modify/$', views.modify_payment, name="modify_payment"),
    url(r'^payments/(?P<id>[0-9a-f-]+)/pay/$', views.pay, name="pay"),
    url(r'^accounts/login/$', 'cas.views.login', name='login'),
    url(r'^accounts/logout/$', 'cas.views.logout', name='logout'),
]

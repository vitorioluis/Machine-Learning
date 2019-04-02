# -*-coding:utf-8
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^', include(('LabsML.core.urls', 'core'), namespace='core')),
    url(r'^ML/', include(('LabsML.ML.urls', 'ML'), namespace='ML')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

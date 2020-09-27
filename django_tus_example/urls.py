"""django_tus_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django_tus.views import TusUpload
from tus_client_demo.views import DemoClientView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', DemoClientView.as_view(), name='demo_client'),
    path('upload/', TusUpload.as_view(), name='tus_upload'),
    path('upload/<uuid:resource_id>', TusUpload.as_view(), name='tus_upload_chunks'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

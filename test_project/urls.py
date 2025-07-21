from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('calc/', views.calc, name='calc'),
    path('calc2/', views.calc2, name='calc2'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('second/', views.second, name='second'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

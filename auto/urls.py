from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from auto.views import *
from .sitemap import SitemapView



schema_view = get_schema_view(
    openapi.Info(
        title="NavisAuto.kg",
        default_version='v1',
        description="Документация Navis auto",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'cars', CarListAPIView)

urlpatterns = [
    path('cars/', CarListAPIView.as_view()),
    path('purchase/', PurchaseRequisitionView.as_view()),
    path('contact/', ContactAPIView.as_view()),

    path("sitemap.xml", SitemapView.as_view()),
    path('NavisAuto/', schema_view.with_ui('swagger', cache_timeout=0)),
]
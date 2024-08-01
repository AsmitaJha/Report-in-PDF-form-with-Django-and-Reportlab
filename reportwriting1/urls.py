from .views import ReportViewSet,MethodologyViewSet,generate_pdf
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from reportwriting1 import views


router=DefaultRouter()
router.register('Report',ReportViewSet,basename='report')
router.register('Methodology',MethodologyViewSet,basename='methodology')

urlpatterns=[
    path('',include(router.urls)),
    path('generate-pdf/', views.generate_pdf, name='generate-pdf')
    ]
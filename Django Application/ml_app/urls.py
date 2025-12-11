"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, index, predict_page,cuda_full

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('predict/', predict_page, name='predict'),
    path('report/', views.report_page, name='report_page'),
    path('report/download/', views.download_report, name='download_report'),
    path('feedback/', views.feedback_page, name='feedback_page'),
    path('feedback/submit/', views.submit_feedback, name='submit_feedback'),
    path('stats/', views.stats_page, name='stats_page'),
    path('cuda_full/',cuda_full,name='cuda_full'),
]

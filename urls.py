from django.urls import path
from . import views


urlpatterns = [

    path('',views.CV,name="CV"),
    path('CV.html',views.test,name="CV_HTML"),
    path('CV.pdf',views.pdf_view, name="PDF")


]
from django.urls import path
from . import views


urlpatterns = [

    path('',views.CV,name="CV"),
    path('CV.html',views.test,name="CV_HTML"),
    path('python_script/', views.python_script, name='script'),
    path('CV.pdf',views.pdf_view, name="PDF")

]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


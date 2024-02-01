import subprocess

from django.shortcuts import render
from .models import allaboutme
from django.http import HttpResponse, FileResponse
from subprocess import run, PIPE
import sys


def CV(request):

    if request.method=="POST":
        info=allaboutme()
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        email = request.POST.get('email')
        descript =request.POST.get('descript')
        phone = request.POST.get('phone')
        linkedin_URL = request.POST.get('linkedin_URL')
        Git_URL = request.POST.get('Git_URL')
        Company1 = request.POST.get('Company1')
        Company2 = request.POST.get('Company2')
        Company3 = request.POST.get('Company3')
        Experience1 = request.POST.get('Experience1')
        Experience2 = request.POST.get('Experience2')
        Experience3 = request.POST.get('Experience3')
        Diplome1 = request.POST.get('Diplome1')
        Description1 = request.POST.get('Description1')
        info.FirstName = Firstname
        info.Lastname = Lastname
        info.email = email
        info.descript = descript
        info.phone = phone
        info.linkedin_URL=linkedin_URL
        info.Git_URL = Git_URL
        info.Company1 = Company1
        info.Company2 = Company2
        info.Company3 = Company3
        info.Experience1 = Experience1
        info.Experience2 = Experience2
        info.Experience3 = Experience3
        info.Diplome1 = Diplome1
        info.Description1 = Description1
        info.save()
    return render(request, 'contact.html')

def test(request):
    try:
        return render(request,'CV.html')
    except:
        return HttpResponse("<b><center>You did not generate your files, please return to the main page and click on the link</center></b>")


def python_script(request):
    run([sys.executable, 'C:\\Users\\Put your path here\\creationPDF.py'], shell=False, stdout=PIPE)
    return HttpResponse("<b><center>Your CV in PDF and HTML format have been created</center></b>")

def pdf_view(request):
    pdf_path = r'C:\Users\Put your path here\template\CV.pdf'
    subprocess.Popen([pdf_path], shell=True)
    return HttpResponse("<b>Your PDF file should be opening now </b>")


    #with open(pdf_path,'rb') as pdf_file:
        #response=FileResponse('pdf_path', content_type='application/pdf')
        #response['Content-Disposition']='inline;filename=CV.pdf'
        #return response






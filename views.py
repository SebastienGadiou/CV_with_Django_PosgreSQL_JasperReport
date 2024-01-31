from django.shortcuts import render
from .models import allaboutme
from django.http import FileResponse, Http404


def CV(request):

    if request.method=="POST":
        info=allaboutme()
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        email = request.POST.get('email')
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

    return render(request,'CV.html')



def pdf_view(request):
    pdf_path = r'C:\Users\Put your path here\template\CV.pdf'
    with open(pdf_path,'rb') as pdf_file:
        response=FileResponse('pdf_path', content_type='application/pdf')
        response['Content-Disposition']='inline;filename=CV.pdf'
        return response



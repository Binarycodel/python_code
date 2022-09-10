import http
from http.client import HTTPResponse
import os
from urllib import response
from django.shortcuts import render, redirect
from .models import StudentUser, ElectronicBook
from django.conf import settings



# Create your views here.


def login(request):
    if request.method == 'POST':
        matric_number = request.POST['matric_num']
        pass_code = request.POST['pass_code']

        print(f'matric : {matric_number} passcode:{pass_code}')
        # auth_student = authenticate(matric_numbr = matric_number.strip() , password= pass_code.strip())
        auth_student = authenticate_student(matric_number, pass_code)
        print(auth_student)

        if auth_student != None :
            if auth_student.validate:
                request.session['matric_number'] = auth_student.matric_number
               
                # getting and all e-book fiel
                ebooks = ElectronicBook.objects.all()
                
                return render(request, 'account.html' , {"ebooks":ebooks, "lens_student":auth_student})
        
        else: 
            return redirect('/')
    else : 
        return render(request, 'login.html')


def account(request):
    try:
        matric = request.session['matric_number']
        stud = list(StudentUser.objects.filter(matric_number=matric))
        if len(stud) == 0:
            return render(request, 'login.html')
        print(stud[0].validate)
        if stud[0].validate:
            print('already validate')
            ebooks = ElectronicBook.objects.all()
            return render(request, 'account.html', {'ebooks':ebooks , 'lens_student':stud[0]})
        else:
            return render(request, 'login.html')
    except KeyError:
        return render(request, 'login.html')

def content(reques):
    print('hellow content')

def authenticate_student(matric_number, pass_code):
        st = None
        stud = StudentUser.objects.filter(matric_number=matric_number, password=pass_code)
        validate_student = False
        if list(stud) != []:
            st = stud[0]
            print('correct credentials.....')
            validate_student = True
            st.validate = True
            st.save()
        else: 
            print('Wrong Credientials......')
            validate_student = False

        return st


def logout(request):
    print('logout called')
    try:
        matric = request.session['matric_number']
        stud = list(StudentUser.objects.filter(matric_number=matric))
        stud[0].validate = False 
        stud[0].save()
        del request.session['matric_number']
        print('operation completed.....')
        return render(request, 'login.html')
    except KeyError:
        return render(request, 'login.html')



def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HTTPResponse(fh.read(),content_type='application/adminupload')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
        
        raise http404
from re import M
from django.shortcuts import render, redirect

from books.views import materials
from .models import Lecturer
from books.models import Materials
from .forms import MaterialForm

import lecturer

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        print(f'Email : {email} password:{password}')
        # auth_student = authenticate(matric_numbr = matric_number.strip() , password= pass_code.strip())
        auth_lecturer = authenticate_lecturer(email, password)
        print(auth_lecturer)

        if auth_lecturer != None :
            if auth_lecturer.validate:
                request.session['email'] = auth_lecturer.email
               
                form = MaterialForm()
            
                return render(request, 'upload_book.html', {'form':form})
        
        else: 
            return redirect('/lecturer')
    else : 
        return render(request, 'lecturer_login.html')
    
    
def authenticate_lecturer(email, password):
        st = None
        stud = Lecturer.objects.filter(email=email, password=password)
        validate_lecturer = False
        if list(stud) != []:
            st = stud[0]
            print('correct credentials.....')
            validate_lecturer = True
            st.validate = True
            st.save()
        else: 
            print('Wrong Credientials......')
            validate_lecturer = False

        return st


def uploadmaterial(request):

    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            print('form save successfully')
            return render(request, 'lecturer_login.html')


def logout(request):
    print('logout called')
    try:
        email = request.session['email']
        stud = list(Lecturer.objects.filter(email=email))
        stud[0].validate = False 
        stud[0].save()
        del request.session['email']
        print('operation completed.....')
        return render(request, 'lecturer_login.html')
    except KeyError:
        return render(request, 'lecturer_login.html')










# def uploadmaterial(request):

#     if request.method == 'POST':
#         course_code = request.POST['coursecode']
#         course_title = request.POST['coursetitle']
#         year = request.POST['year']
#         level = request.POST['level']
#         dept = request.POST['department']
#         file = request.POST['file']
#         print(file)

#         # print(f' file : {file} course code : {course_code}')
#         # Materials.objects.create()
#         # if course_code.strip() != '' and course_title.strip() != '' and year.strip() != '' and level != '' and dept != '' and file != None:
#         email = request.session['email']
#         if email != None:

#             # Getting user information first
#             lec = list(Lecturer.objects.filter(email=email))[0]
            
#             form = UploadFileForm(request.POST, request.FILES)
#             print(form)
#             if form.is_valid():
#                 handout = Materials(lecturer=lec.name,course_code=course_code.upper(), course_title=course_title, year=year, level=level,  department=dept ,efile=file)
#                 handout.save()
#                 print('upload sucessfully')
#                 return redirect(request, 'lecturer_login.html')
#             else:
#                 form = UploadFileForm()
#                 print('uploading not successfull')
#                 return render(request, 'upload.html')

#         return render(request, 'lecturer_login.html')


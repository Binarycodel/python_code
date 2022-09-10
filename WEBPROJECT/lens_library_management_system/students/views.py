from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
# from .models import StudentsUser
# Create your views here.



def account(request):
    return render(request, 'account.html')


def login(request):
    
    # if request.method == 'POST':
    #     matric_number = request.POST['matric_num']
    #     pass_code = request.POST['pass_code']

    #     print(f'matric : {matric_number} passcode:{pass_code}')
    #     auth_student = authenticate(matric_numbr = matric_number.strip() , password= pass_code.strip())
    #     student = authenticate_student(matric_number, pass_code)
    #     print(auth_student)

    #     if student.validate: 
    #         return render(request, 'account.html')
    #     # else: 
    #     #     return redirect('/')
    # else : 
    return render(request, 'login.html')
    # return redirect('/')
    # else:
    #     print('Nothing happens...')
    #     return render(request, 'login.html')


# def authenticate_student(matric_number, pass_code):
#         stud = Students.objects.filter(matric_number=matric_number, password=pass_code)
#         validate_student = False
#         if list(stud) != []:
#             st = stud[0]
#             print('correct credentials.....')
#             validate_student = True
#             st.validate = True
#             st.save()
#         else: 
#             print('Wrong Credientials......')
#             validate_student = False

#         return st



# def invalidate_student():
#     print(Students.validate) 



        
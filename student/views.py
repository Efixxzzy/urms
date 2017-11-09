from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *
from subject.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        username = request.POST.get('rollno')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            context = {
                'error_message': 'Invalid Roll Number/Password'
            }
            return render(request, 'login.html', context)

@login_required
def home(request):
    return render(request, 'home.html', {})

@login_required
def student(request):
    student_obj, created = Student.objects.get_or_create(user=request.user)

    if student_obj.locked:
        return render(request, 'home.html', {'error_message': "Your form has already been locked."}) 

    if request.method == 'GET':
        return render(request, 'student.html', {'student':student_obj})
    elif request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        contact_number = int(request.POST.get('contact_number'))

        if name and date_of_birth and address and 7000000000 <= contact_number <= 9999999999:
            student_obj.name = name
            student_obj.date_of_birth = date_of_birth
            student_obj.address = address
            student_obj.contact_number = contact_number
            student_obj.save()
            return redirect('/subject')
        else:
            return render(request, 'student.html', {'error_message':'Invalid form values'})

@login_required
def subject(request):
    student_obj, created = Student.objects.get_or_create(user=request.user)
    if student_obj.locked:
        return render(request, 'home.html', {'error_message': "Your form has already been locked."}) 
    
    if not student_obj.name:
        return redirect('/student')

    subject_list = student_obj.stream.subject_set
    if request.method == 'GET':
        return render(request, 'subject.html', {
            'regular_subjects': subject_list.filter(type='Regular'),
            'reregister_subjects': subject_list.filter(type='Re-register')
        })

    elif request.method == 'POST':
        # print(request.POST)
        student_obj.courses.clear()
        for subject in subject_list.all():
            if request.POST.get(subject.code):
                pk = request.POST.get(subject.code)
                course = Course.objects.get(pk=pk)
                student_obj.courses.add(course)
        return redirect('/final')

@login_required
def final(request):
    student_obj, created = Student.objects.get_or_create(user=request.user)
    
    if student_obj.locked:
        return render(request, 'home.html', {'error_message': "Your form has already been locked."}) 
    
    if not student_obj.courses:
        return redirect('/subject')

    if request.method == 'GET':
        return render(request, 'final.html', {})
    elif request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        if transaction_id:
            student_obj.transaction_id = transaction_id
            student_obj.locked = True
            student_obj.save()
            return redirect('/')
        else:
            return render(request, 'final.html', {'error_message':'Invalid form values'})

@login_required
def admit_card(request):
    student_obj, created = Student.objects.get_or_create(user=request.user)
    if not student_obj.locked:
        return render(request, 'home.html', {'error_message': "Your form has not been locked."}) 

    return render(request, 'admit_card.html', {'student': student_obj})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/login')



            

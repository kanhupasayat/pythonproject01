from .models import User, StudentUpdate
from .models import StudentUpdate   # Import your User model
from .models import User
from django.shortcuts import render, get_object_or_404
from .models import User  # Import your model
from .models import StudentUpdate
from .forms import UserUpdateForm  # Import the UserUpdateForm
from django.shortcuts import render, get_object_or_404, redirect
import email
from django.shortcuts import render

# Create your views here.


from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, redirect
from .models import Student01


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                messages.info(request, 'login successfull you admin')
                return redirect('user_list/')
            else:
                login(request, user)
                messages.info(request, 'login successfull')
                return redirect('index2/')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/')


@login_required(login_url="/")
def student_list(request):
    students = Student01.objects.all()  # Retrieve all student records

    context = {
        'students': students  # Pass the data to the template context
    }

    return render(request, 'student_list.html', context)


# this is code===========


# @login_required(login_url="/")
# def student(request):
#     if request.method == "POST":
#         data = request.POST
#         first_name = data.get('first_name')
#         last_name = data.get('last_name')
#         user_name = data.get('username')   # this is mobile number
#         password = data.get('password')
#         email = data.get('email')
#         print("kanhu")

#         user = User.objects.filter(username=user_name)
#         mail = User.objects.filter(email=email)

#         if user.exists():
#             messages.info(request, 'Username already taken')
#             return redirect('/student/')

#         # Check for email uniqueness (uncomment this if you want to check for email uniqueness)
#         # if mail.exists():
#         #     messages.info(request, 'Email already taken')
#         #     return redirect('/student/')

#         # Create a Django User instance
#         user = User.objects.create(
#             username=user_name,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#         )
#         user.save()

#         user.set_password(password)
#         user.save()

#         # Create the Student01 instance with the phone number

#         messages.info(request, 'Account created successfully')
#         return redirect('/student/')

#     return render(request, 'student.html')


#=======table user account========
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student02
from django.contrib.auth.models import User

def student(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_name = data.get('username')   # this is mobile number
        password = data.get('password')
        email = data.get('email')

        user = User.objects.filter(username=user_name)
        mail = User.objects.filter(email=email)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/student/')

        # Check for email uniqueness (uncomment this if you want to check for email uniqueness)
        # if mail.exists():
        #     messages.info(request, 'Email already taken')
        #     return redirect('/student/')

        # Create a Django User instance
        user = User.objects.create(
            username=user_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.save()

        user.set_password(password)
        user.save()

        # Create the Student01 instance with the phone number
        student = Student02.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=user_name,
            email=email,
        )
        student.save()

        messages.info(request, 'Account created successfully')
        return redirect('/student/')

    students = Student02.objects.all()  # Fetch all students from the database
    return render(request, 'student.html', {'students': students})











# =========delete user==========


@login_required(login_url="/")
def delete_user(request, username):
    try:
        user_to_delete = User.objects.get(username=username)
        user_to_delete.delete()
        print("yes")
        return redirect('user_list')
    except User.DoesNotExist:
        # Handle the case where the user does not exist, e.g., show an error message
        # or redirect to another page.
        # You can customize this behavior as needed
        return redirect('user_list')


# =======update====first name===lastname===email=====


# views.py


@login_required(login_url="/")
def update_user(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to a success page or user profile page
            # Change 'user_profile' to your actual profile view name
            return redirect('/index2/')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'update_user.html', {'user': user, 'form': form})


# =========student login home page=========

@login_required(login_url="/")
def index2_page(request):
    if request.method == "POST":
        user_course = request.POST.get('user_course')
        user_room = request.POST.get('user_room')
        user_start = request.POST.get('user_start')
        user_end = request.POST.get('user_end')
        current_date = request.POST.get('current_date')
        current_day = request.POST.get('current_day')

        try:
            # Get the authenticated user
            authenticated_user = request.user
            user_name = authenticated_user.first_name
            user_mobile = authenticated_user.username

            # Create a StudentUpdate instance and associate it with the authenticated user
            StudentUpdate.objects.create(
                user=authenticated_user,
                user_mobile=user_mobile,
                user_name=user_name,
                user_course=user_course,
                user_room=user_room,
                user_start=user_start,
                user_end=user_end,
                current_date=current_date,
                current_day=current_day,
            )

            messages.info(request, 'Submission successful')
            # Redirect to a success page or wherever you want
            return redirect('/index2/')

        except Exception as e:
            print("An error occurred:", e)
            messages.error(request, 'An error occurred during submission')

    return render(request, 'index2.html')


# change_password
@login_required(login_url="/")
def Change_Password(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(
                request, 'Your Password Has Be Changed Succesfully......')
            return redirect('/')

    else:
        fm = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'fm': fm})


@login_required(login_url="/")
def index_page(request):
    if request.method == "POST":
        user_course = request.POST.get('user_course')
        user_room = request.POST.get('user_room')
        user_start = request.POST.get('user_start')
        user_end = request.POST.get('user_end')
        current_date = request.POST.get('current_date')
        current_day = request.POST.get('current_day')

        try:
            # Get the authenticated user
            authenticated_user = request.user

            # Create a StudentUpdate instance and associate it with the authenticated user
            StudentUpdate.objects.create(
                user=authenticated_user,
                user_course=user_course,
                user_room=user_room,
                user_start=user_start,
                user_end=user_end,
                current_date=current_date,
                current_day=current_day,
            )

            messages.info(request, 'Submission successful')
            # Redirect to a success page or wherever you want
            return redirect('/index/')

        except Exception as e:
            print("An error occurred:", e)
            messages.error(request, 'An error occurred during submission')

    return render(request, 'index.html')


@login_required(login_url="/")
def search_page(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        if query:
            student_updates = StudentUpdate.objects.filter(
                user__first_name__icontains=query)

        else:
            student_updates = StudentUpdate.objects.all()
    else:
        student_updates = StudentUpdate.objects.all()
        query = ""

    context = {
        'student_updates': student_updates[::-1],
        'query': query,
    }

    return render(request, 'search_page.html', context)


# views.py


@login_required(login_url="/")
def show_data(request):
    if request.method == 'POST':
        query = request.POST.get('user_mobile')
        if query:
            show_data = User.objects.filter(username__icontains=query)
            print("kanhu")
        else:
            show_data = User.objects.all()
            print("else")
    else:
        show_data = User.objects.all()
        query = ""

    context = {
        'show_data': show_data[::-1],
        'query': query,
    }

    return render(request, 'show_data.html', context)


@login_required(login_url="/")
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users[::-1]})


@login_required(login_url="/")
def user_detail(request, username):
    # Retrieve the user object based on the provided username
    user = get_object_or_404(User, username=username)

    return render(request, 'user_detail.html',)


@login_required(login_url="/")
def user_detail(request, username):
    users = User.objects.all()
    # Retrieve the user object based on the provided username
    user = get_object_or_404(User, username=username)

    # Query the StudentUpdate model to get updates related to the user
    student_updates = StudentUpdate.objects.filter(user=user)

    context = {
        'users': users,
        'student_updates': student_updates[::-1],
    }

    return render(request, 'user_detail.html', context)


@login_required(login_url="/")
def show_page(request):
    student_updates = StudentUpdate.objects.all()
    return render(request, 'show.html', {'student_updates': student_updates[::-1]})


@login_required(login_url="/")
def show_user_page(request):
    user = request.user
    student_updates = StudentUpdate.objects.filter(user=user)
    return render(request, 'show_user_page.html', {'student_updates': student_updates[::-1]})




import pandas as pd
from django.http import HttpResponse

from .models import StudentUpdate

def export_data_to_excel(request):
    data =StudentUpdate.objects.all()
    df = pd.DataFrame(data.values())  # Convert data to a pandas DataFrame

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    df.to_excel(response, index=False, engine='openpyxl')
    return response


from .models import Student02

def export_data_to_excel2(request):
    data = Student02.objects.all()
    
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data.values())

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    df.to_excel(response, index=False, engine='openpyxl')
    return response












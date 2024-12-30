from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import Record
import logging
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 

# Create your views here.

# @login_required(login_url='website:home')
def home(request):
    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authentication 

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You Have Been Logged In!')
            return redirect('website:home')
        else:
            messages.success(request, 'There Was An Error Logging In, Please Try Again')
            return redirect('website:home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Logged Out...')
    return redirect('website:home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('website:home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You Must Be Logged In To View That Page...')
        return redirect('website:home')


def delete_record(request, pk):
     if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record Deleted Successfully!')
        return redirect('website:home')
     else:
        messages.success(request, 'You Must Be Logged In To Delete That Record...')
        return redirect('website:home')
          
def add_record(request):
        form = AddRecordForm(request.POST or None)
        if request.user.is_authenticated:
            if request.method == "POST":
                if form.is_valid():
                    add_record = form.save()
                    messages.success(request,'Record Added...')
                    return redirect('website:home')
        else:
            messages.success(request,'You Must Be Logged In')
            return redirect('website:home')
        return render(request, 'add_record.html', {'form':form})
     

def update_record(request, pk):
        if request.user.is_authenticated:
            current_record = Record.objects.get(id=pk)
            form = AddRecordForm(request.POST or None, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request,'Record Has Been Updated!')
                return redirect('website:home')
            return render(request, 'update_record.html', {'form':form})
        else:
            messages.success(request,'You Must Be Logged In')
            return redirect('website:home')
             


def custom_page_not_found(request,exception):
     return render(request,'404.html',status=404)

logger = logging.getLogger(__name__)

def search(request):
    if request.user.is_authenticated:
        query= request.GET.get('query')
        results =[]
        try:
            if query:
                results= Record.objects.filter(Q(first_name__icontains=query)| Q(last_name__icontains=query) | Q(id__icontains=query))
        except Exception as e:
          logger.error('Error during search: %s',e)
          
        return render(request,'search.html',{'results':results, 'query':query})
    else:
         messages.success(request,'You Must Be Logged In')
         return redirect('website:home')
    
def profile(request):
     if request.user.is_authenticated:
        return render(request,'profile.html',{})
     


def trigger_error(request):
    return render(request, '500.html', status=500)


def cause_error(request):
      # هذا الكود يتسبب في خطأ القسمة على صفر 
      result = 1 / 0 
      return HttpResponse(f"النتيجة: {result}")
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'job-admin/login.html')  


def view(request):
    return render(request,'job-admin/view.html')    
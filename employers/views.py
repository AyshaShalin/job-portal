from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'employers/login.html')



def dashboard(request):
    return render(request,'employers/homepage.html')

def signup(request):
    return render(request,'employers/sign Up.html')    

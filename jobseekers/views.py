from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'jobseekers/login.html')

def searchjob(request):
    return render(request,'jobseekers/jobsearch.html')


def jobdetails(request):
    return render(request,'jobseekers/jobdetails.html')    
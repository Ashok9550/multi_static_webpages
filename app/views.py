
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')
def sign_in(request):
    return render(request,'sign_in.html')
def sign_up(request):
    return render(request,'sign_up.html')
def course(request):
    return render(request,'course.html')
def forgoted(request):
    return render(request,'forgoted.html')
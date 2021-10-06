from django.shortcuts import render,HttpResponse,redirect

def project_list(request):
    return render(request,'web/project_list.html')
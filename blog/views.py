from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post, Category, Tag
from blog.forms import UserForm
#from django.template import RequestContext


def blog_list(request):
    blogs = Category.objects.all().order_by('-publish_time')
    return render(request,'index.html',{"blogs":blogs})


def register(request):
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            print forms.cleaned_data
            return HttpResponse('ok')
    else:
        forms = UserForm()

    return render(request,'register.html',{'forms':forms})

def register1(request):
    return render(request,'register1.html',)

def message(request):
    username = request.GET.get("username","")
    sex = request.GET.get("sex","")
    hobby = request.GET.get("hobby","")
    return HttpResponse(username+sex+hobby)
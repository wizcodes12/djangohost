from django.http import HttpResponse
from distutils.command.upload import upload
from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render




# class UserAuthModel(AbstractUser):
#     userProfile=models.ImageField(upload_to='UserProfile')


# class Category(models.Model):
#     title = models.CharField(max_length=200)
#     desciption = models.TextField()


#     def __str__(self):
        





def index(request):
    # params={'name':'wizcodes','place':'yt'}
    return render(request,'index.html')
    # return HttpResponse('''<h1><a href="https://www.youtube.com/results?search_query=django+project+download+tourist+system">Click Me </a></h1>''')


def about(request):
    return HttpResponse("see about")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif removepunc == "off":
        return render(request,'off.html')
    
    else:
        return render(request,'error.html')
    

def submit(request):
    djtext = request.GET.get('text', 'default')
    submit = request.GET.get('removepunc')
    if submit=='true':
        return render(request,'submit.html')
    
    

# class Signup(CreateView):
#     f 
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect
from .forms import FileForm
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def text(request):
    params = {
        'post_msg': None,
    }
    if request.method=='POST':
        params['post_msg'] = request.POST['post_text']

    return render(request, 'main/text.html', params)

def jstext(request):
    params = {
        'js_text': None,
    }
    if(request.method=='POST'):
        params['js_text'] = request.POST['js_text']

    return render(request, 'main/jstext.html', params)

def files(request):
    params = {
        'form': FileForm(),
        'file_obj': None,
    }

    if request.method=='POST':
        file_obj = request.FILES['file']
        params['file_obj'] = file_obj

    return render(request, 'main/files.html', params)


def put(request):
    params = {
        'put_text': None
    }
    if request.method=='PUT':
        data = dict(QueryDict(request.body))
        for key in data:
            params['put_text'] = key
    
    print(params)
    return render(request, 'main/put.html', params)

def zero(request):
    return render(request, 'main/zero.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {

    }
    return render(request, 'main/index.html', params)

def text(request):
    if(request.method=="POST"):
        msg = request.POST['text']
    else:
        msg = '何かを入力してください'
    params = {
        'msg': msg
    }
    return render(request, 'main/text.html', params)

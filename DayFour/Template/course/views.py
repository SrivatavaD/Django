from django.http import HttpResponse

# Create your views here.


def learn_django(req):
    return HttpResponse('Learn Django')


def learn_python(req):
    return HttpResponse('Learn Python')

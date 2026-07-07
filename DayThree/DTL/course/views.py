from django.shortcuts import render

# Create your views here.
# def learn_django(req):
#     return render(req, 'course/django.html', context = {'name': 'Django', 'Status': 'ok'})

def learn_django(req):
    name = 'Django'
    duration = '4 Months'
    Seats = 10
    Course_details = {'name': name, 'duration': duration, 'Seats': Seats}
    return render(req, 'course/django.html')
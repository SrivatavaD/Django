from django.shortcuts import render

def learn_django(req):

    return render(req, template_name, context=dic_name,
                  content_type=MIME_TYPE, status=None, using=None)
                  
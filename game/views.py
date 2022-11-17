from django.http import HttpResponse

def index(request):
    line1 = '<h1 style = "text-align: center"> A Web Here</h1>'
    line2 = '<img src = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg">'
    return HttpResponse(line1 + line2)

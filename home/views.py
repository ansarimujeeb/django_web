from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    data = {
        "variable1": "Im a graete",
        "varaible2": "You are a great"
    }
    return render( request, 'index.html', data)

def about(request):
    return render( request, 'about.html')
    # return HttpResponse("This is the about page")

def service(request):
    return render( request, 'services.html')

def contact(request):
    return render( request, 'contact.html')

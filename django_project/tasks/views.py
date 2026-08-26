from django.http import HttpResponse #Libreria para dar respuestas http

# Create your views here.
def home(request):
    return HttpResponse("Hello, This my firts application")
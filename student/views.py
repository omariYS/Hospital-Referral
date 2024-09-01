from django.shortcuts import render
#from django.shortcuts import HttpResponse

#def home_page(request):
#    return HttpResponse("Hello Omar, you are in the Student index.") 

def home_page(request):
    return render(request, 'home.html') #This maps home_page request to home.html


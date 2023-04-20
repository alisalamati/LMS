from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
# declare views function

def vw_login(request):
    return render(request, "login.html")
    #return HttpResponse("<h2 style='color:blue;'>Login pages...</h2>")

def vw_logout(request):
    return render(request, "logout.html")
    #return HttpResponse("<h2 style='color:red;'>Logout Pages...</h2>")

def vw_home(request):
    class User:
        def __init__(self, username, city):
            self.Username = username
            self.City = city

    user_obj = User("Ali", "Tehran")
    return render(request, "home.html", {"user": user_obj})
   # return HttpResponse("<h1 style='color:green;'>Home Pages....</h1>")

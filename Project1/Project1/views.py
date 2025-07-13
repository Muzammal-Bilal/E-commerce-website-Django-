from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import login

def home(request):
    """
    Render the home page.
    """

    # data={
    #     "name": "Muzammal Bilal",
    #     "age": 20,
    #     "city": "Karachi",
    #     "country": "Pakistan",
    #     "course" : ["Python", "Django", "JavaScript", "HTML", "CSS"],
    #     "studentdetail" :[{"name": "Muzammal Bilal","age": 20,"city": "Karachi","country": "Pakistan"},
    #                {"name": "Ali","age": 22,"city": "Lahore","country": "Pakistan"},
    #                {"name": "Sara","age": 19,"city": "Islamabad","country": "Pakistan"}]
    # }
    return render(request, "index.html")

def blog(request):
    """
    Render a page with a custom message.
    """
     
    return render(request, "blog.html")

def account(request):
    try:
        form={"form":login}
        if request.method == "POST":
                # Handle form submission
                # For example, you can access form data like this:
            username = request.POST.get("username")
            password=request.POST.get("password")
            print(f"Username: {username}, Password: {password}")
            data={"username": username, "password": password}
            form={"form":login}
            return redirect ("/cart/")
    except:
        print("Username or password not provided in the request.")
    return render(request, "account.html",form)

def contact(request):
    """
    Render a page with a custom message.
    """
    

    return render(request, "contact.html")

def shop(request):
    """
    Render a page with a custom message.
    """
    
    return render(request, "shop.html")

def cart(request):
    """
    Render a page with a custom message.
    """
    
    return render(request, "cart.html")

def single_product(request):
    """
    Render a page with a custom message.
    """
    
    return render(request, "single-product.html")

def single_blog(request):
    """
    Render a page with a custom message.
    """
    
    return render(request, "single-blog.html")
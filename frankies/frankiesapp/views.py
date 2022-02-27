from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'frankiesapp/hello_world.html')

def add_product(request):
    return render(request, 'frankiesapp/add_product.html')
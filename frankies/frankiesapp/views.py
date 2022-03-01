from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def hello_world(request):
    return render(request, 'frankiesapp/hello_world.html')


#USER VIEW
def view_products(request):
    product_objects = Product.objects.all
    return render(request, 'frankiesapp/view_products.html',{'products':product_objects} )


#ADMIN VIEW

def add_product(request):
    if(request.method=="POST"):
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_image = request.POST.get('product_imagee')
        product_materialsused = request.POST.get('product_materialsused')
        product_quantity = request.POST.get('product_quantity')
        product_unitprice = request.POST.get('product_unitprice')
        product_type = request.POST.get('product_type')
        product_visibility = request.POST.get('product_visibility')
        product_colors1 = request.POST.get('product_colors1')
        product_colors2 = request.POST.get('product_colors2')
        product_colors3 = request.POST.get('product_colors3')
        product_colors4 = request.POST.get('product_colors4')
        product_colors5 = request.POST.get('product_colors5')
        product_colors6 = request.POST.get('product_colors6')
        product_colors7 = request.POST.get('product_colors7')
        product_colors8 = request.POST.get('product_colors8')

        try:
            Product.objects.create(product_id=product_id,
            product_name=product_name, 
            product_description=product_description, 
            product_image=product_image,  
            product_materialsused= product_materialsused,  
            product_quantity= product_quantity, 
            product_unitprice=product_unitprice, 
            product_type=product_type, 
            product_visibility=product_visibility, 
            product_colors1=product_colors1,
            product_colors2=product_colors2,
            product_colors3=product_colors3,
            product_colors4=product_colors4,
            product_colors5=product_colors5,
            product_colors6=product_colors6,
            product_colors7=product_colors7,
            product_colors8=product_colors8)


            message = "Product created successfully"
            return render(request, 'frankiesapp/add_product.html', {'message':message})
    
        except Exception as e:
            message = e
            context = {'message':message}
            return render(request, 'frankiesapp/add_product.html', context)

    else:
        return render(request, 'frankiesapp/add_product.html')

    return render(request, 'frankiesapp/add_product.html')
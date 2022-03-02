from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.
def hello_world(request):
    return render(request, 'frankiesapp/hello_world.html')


#CUSTOMER VIEW
def view_products(request):
    product_objects = Product.objects.all()
    product_collection = Product_Collection.objects.all()
    return render(request, 'frankiesapp/view_products.html',{'products':product_objects, 'product_collection':product_collection} )


def view_productdetails(request, pk):
    productdetails = get_object_or_404(Product, pk=pk)
    return render(request,'frankiesapp/view_productdetails.html',{'p':productdetails})


#ADMIN VIEW
def add_productcollection(request):
    prodColl_objects = Product_Collection.objects.all()
    if(request.method == "POST"):
        productcollection = request.POST.get('productcollection')

        # PRODUCT COLLECTION LIST
        plist = Product_Collection.objects.filter()
        plistlower = []
        for p in plist:
            clower = p.getProductColl().lower()
            plistlower.append(clower)
        
        # if collection already exists
        if(productcollection.lower() in plistlower):
            message = "Collection already exists"
            return render(request, 'frankiesapp/add_productcollection.html',{'prodColl':prodColl_objects, 'message':message})
        else:
            Product_Collection.objects.create(productcollection_name=productcollection)
            return render(request, 'frankiesapp/add_productcollection.html',{'prodColl':prodColl_objects})
    else:    
        return render(request, 'frankiesapp/add_productcollection.html',{'prodColl':prodColl_objects})

def update_productcollection(request,pk):
    if(request.method == "POST"):
        productcollection = request.POST.get('updateproductcollection')
        pc = get_object_or_404(Product_Collection, pk=pk)

        productollection_lower = productcollection.lower()
        plist = Product_Collection.objects.filter()
        plistlower = []
        for p in plist:
            clower = p.getProductColl().lower()
            plistlower.append(clower)

        # if the collection is the same
        if(productcollection.lower() == pc.getProductColl().lower()):
            message = "Please enter a different collection name"
            return render(request, 'frankiesapp/update_productcollection.html', {'message':message,'pc': pc})

        # if the collection already exists
    
        elif(productollection_lower in plistlower):
            message = "Collection already exists"
            return render(request, 'frankiesapp/update_productcollection.html', {'message':message,'pc': pc})

        else:
            Product_Collection.objects.filter(pk=pk).update(productcollection_name = productcollection)
            message = "Successfully changed collection name"
            return redirect(add_productcollection)
    else:
        pc = get_object_or_404(Product_Collection, pk=pk)
        return render(request, 'frankiesapp/update_productcollection.html',{'pc':pc})

def delete_productcollection(request,pk):
    Product_Collection.objects.get(pk=pk).delete()
    return redirect(add_productcollection)

def view_product(request):
    admin_productlist = Product.objects.all()
    
    return render(request, 'frankiesapp/admin_productlist.html', {'product':admin_productlist})

def add_product(request):
    pc = Product_Collection.objects.all()
    if(request.method=="POST"):

        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_collectionpk = request.POST.get('product_collection')
        product_collection = Product_Collection.objects.get(pk=product_collectionpk)
        product_description = request.POST.get('product_description')
        product_image = request.POST.get('product_image')

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
            product_collection=product_collection, 
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
        return render(request, 'frankiesapp/add_product.html', {'pc':pc})

    return render(request, 'frankiesapp/add_product.html')
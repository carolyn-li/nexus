from django.db import models

# Create your models here.
class Product(models.Model): #FIX THIS JANSEN CHANGE THE CHARFIELDS
    product_id = models.CharField(max_length=300, primary_key=True)
    #product_collection = models.ForeignKey(Product_Collection, on_delete=models.CASCADE) Wait for CJ's class or remove 
    product_name = models.CharField(max_length=300)
    product_description = models.TextField(max_length=300)
    product_image = models.FileField(upload_to=None) #upload and display image
    product_materialsused = models.CharField(max_length=300) #collection of materials
    product_quantity = models.IntegerField(max_length=10)
    product_unitprice = models.IntegerField(max_length=10)
    product_type = models.CharField(max_length=300) #list of copllections but can add
    product_visibility = models.BooleanField(max_length=300) #Visibility switch
    product_colors = models.CharField(max_length=300) #Probably a list of colors

    def __str__(self):#DONT KNOW IF THIS IS NEEDED
        return f"{self.product_id}, {self.product_name}, {self.product_description}, {self.product_image}, {self.product_materialsused}, {self.product_quantity}, {self.product_unitprice}, {self.product_type}, {self.product_visibility}, {self.product_colors}"

class Material(models.Model): 
    material_id = models.CharField(max_length=300)
    material_name = models.CharField(max_length=300)
    material_image = models.CharField(max_length=300)
    material_supplierlink = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.material_id}, {self.material.name}, {self.material_image}, {self.material_supplierlink}"

class Admin(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def getUsername(self):
        return f"{self.username}"

    def getPassword(self):
        return f"{self.password}"

    def __str__(self):
        return f"{self.pk}: {self.username}"
    

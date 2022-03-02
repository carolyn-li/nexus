from django.db import models

# Create your models here.
class Product_Collection(models.Model):
    # productcollection_id = models.CharField(max_length=300, primary_key=True, unique=True)
    productcollection_name = models.CharField(max_length=300)
    objects = models.Manager()

    def getProductColl(self):
        return self.productcollection_name

    def __str__(self):
        return f"{str(self.pk)} - {self.productcollection_name}"
        
class Product(models.Model): 
    product_id = models.CharField(max_length=300, primary_key=True, unique=True)
    product_collection = models.ForeignKey(Product_Collection, on_delete=models.CASCADE, null=True) 
    product_name = models.CharField(max_length=300)
    product_description = models.TextField(max_length=300)
    product_image = models.FileField(null=True, blank=True, upload_to='toProcess/') #upload and display image
    product_materialsused = models.CharField(max_length=300) 
    product_quantity = models.PositiveIntegerField()
    product_unitprice = models.PositiveIntegerField()
    product_type = models.CharField(max_length=300) #list of copllections but can add
    product_visibility = models.CharField(max_length=300) #Visibility switch
    product_colors1 = models.CharField(max_length=300) #Probably a list of colors
    product_colors2 = models.CharField(max_length=300)
    product_colors3 = models.CharField(max_length=300)
    product_colors4 = models.CharField(max_length=300)
    product_colors5 = models.CharField(max_length=300)
    product_colors6 = models.CharField(max_length=300)
    product_colors7 = models.CharField(max_length=300)
    product_colors8 = models.CharField(max_length=300)


    def __str__(self):
        return f"{self.product_id}, {self.product_name}, {self.product_description}, {self.product_image}, {self.product_materialsused}, {self.product_quantity}, {self.product_unitprice}, {self.product_type}, {self.product_visibility}, {self.product_colors1}, {self.product_colors2}, {self.product_colors3}, {self.product_colors4}, {self.product_colors5}, {self.product_colors6}, {self.product_colors7}, {self.product_colors8}, "

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
    

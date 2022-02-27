from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.field(max_length=300)
    product_name = models.Charfield(max_length=300)
    product_description = models.Charfield(max_length=300)
    product_image = models.Charfield(max_length=300)
    product_materialsused = models.Charfield(max_length=300)
    product_collection = models.Charfield(max_length=300)
    product_quantity = models.Charfield(max_length=300)
    product_unitprice = models.Charfield(max_length=300)
    product_type = models.Charfield(max_length=300)
    product_visibility = models.Charfield(max_length=300)
    product_colors = models.Charfield(max_length=300)

    def __str__(self):
        return f"{self.product_id}, {self.product_name}, {self.product_description}, {self.product_image}, {self.product_quantity}, {self.product_unitprice}, {self.product_type}, {self.product_visibility}"

class Material(models.Model):
    material_id = models.field(max_length=300)
    material_name = models.Charfield(max_length=300)
    material_image = models.Charfield(max_length=300)
    material_supplierlink = models.Charfield(max_length=1000)

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
    

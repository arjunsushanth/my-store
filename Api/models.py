from django.db import models
from django.contrib.auth.models import User
from  django.core.validators import MinValueValidator,MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    catagory = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to="image")

    @property
    def avg_rating(self):
        rating=self.review_set.all().values_list('rating',flat=True)
        if rating:
            return sum(rating)/len(rating)
        else:
            return 0

    @property
    def review_count(self):
        rating = self.review_set.all().values_list('rating', flat=True)
        if rating:
            return sum(rating)
        else:
            return 0



    def __str__(self):
        return self.name
class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    options=(
        ("order-placed","order-placed"),
        ("in-cart","in-cart"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
   


class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    comment=models.CharField(max_length=200)

class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("despathed","despatched"),
        ("in-transit","in-transit"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    data=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)








#modelname.object.create(field=value1,field2=value2)
#prroduct.objects.create(name="pi",price=2500,description="mobile",category="electronics")
#qs=models.objects.all()
#qs=Product.objects.filter(category="electronics")
#qs=products.objects.all().exclude(catagory="electronics")
#qs=product.object.get(id=1)

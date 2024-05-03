from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Catgory(models.Model):

    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub')
    sub_cat=models.BooleanField(default=False)
    name=models.CharField(max_length=200)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    slug=models.SlugField(allow_unicode=True,unique=True,null=True,blank=True)
    image=models.ImageField(upload_to='category',null=True,blank=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category',args=[self.slug,self.id])


class Product(models.Model):
    VARIANT=(
        ('None','none'),
        ('Size','size'),
        ('Color','color'),
    )

    category=models.ManyToManyField(Catgory,blank=True)
    name= models.CharField(max_length=200)
    amount= models.PositiveIntegerField()
    unit_price=models.PositiveIntegerField()
    discount= models.PositiveIntegerField(blank=True, null=True)
    total_price=models.PositiveIntegerField()
    information=models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    available= models.BooleanField(default=True)
    status = models.CharField(blank=True, null=True,max_length=200,choices=VARIANT)
    image=models.ImageField(upload_to='product')


    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if not self.discount:
          return self.unit_price
        elif self.discount:
            total=(self.discount * self.unit_price) / 100
            return int(self.unit_price-total)
        return self.total_price


class Size(models.Model):
    name=models.CharField(max_length=100)


class Color(models.Model):
    name=models.CharField(max_length=200)


class Vareiants(models.Model):
    name=models.CharField(max_length=100)
    product_variant= models.ForeignKey(Product,on_delete=models.CASCADE)
    size_variant= models.ForeignKey(Size,on_delete=models.CASCADE)
    color_variant= models.ForeignKey(Color,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.EmailField(max_length=200, null=True)
	phone = models.IntegerField(null=False)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models. SlugField(max_length=255)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
		
class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=255, null=True)
	in_stock = models.BooleanField(default=True)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)


	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
		

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
				return str(self.id)

	@property
	def get_cart_total(self):
			orderitems = self.orderitem_set.all()
			total = sum([item.get_total for item in orderitems])
			return total

	@property
	def get_cart_items(self):
			orderitems = self.orderitem_set.all()
			total = sum([item.quantity for item in orderitems])
			return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
			total = self.product.price * self.quantity
			return total

	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=True)
	State = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

		
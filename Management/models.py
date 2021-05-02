from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import *


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('designation', "Manager")

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class Staff(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=50,primary_key = True)
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.CharField(max_length=150, blank=True,null=True)
    dob = models.CharField(max_length=150, blank=True,null=True)
    CATEGORY = [
    ['Manager', 'Manager'],
    ['Cook', 'Cook'],
    ['Waiter', 'Waiter'],
    ['DeliveryBoy', 'DeliveryBoy'],
    ]
    salary = models.IntegerField(null= True)
    designation = models.CharField(max_length = 50,choices = CATEGORY)
    building_no = models.CharField(null= True,max_length=50)
    street_name = models.CharField(max_length=50,null= True)
    city = models.CharField(max_length=50,null= True)
    zipcode = models.IntegerField(null= True)
    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    
    def address(self):
        return f"{self.building_no  +  self.street_name + self.city }"
    def __str__(self):
        return f"{self.user_name}"
    

    
    

class Customer(models.Model):
    id = models.CharField(max_length=50,primary_key = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    times_ordered = models.IntegerField(default = 0)
    def __str__(self):
        return f"{self.first_name + ' ' + self.last_name}"
    def full_name(self):
        return f"{self.first_name + self.last_name}"
    
    
class Customer_phoneNo(models.Model):
    id = models.CharField(max_length=50,primary_key = True)
    phone_number = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="cpno")
    
    def __str__(self):
        return f"{self.phone_number}"
    
class Staff_phoneNo(models.Model):
    id = models.CharField(max_length=50,primary_key = True)
    phone_number = models.IntegerField()
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="sphno")
    def __str__(self):
        return f"{self.staff.user_name + ' ' +  str(self.phone_number)}"
    
class Menu(models.Model):
    id = models.CharField(max_length=50,primary_key = True)
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    category = models.CharField(max_length = 50)
    timesOrdered = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.name}"
 
class Order(models.Model):
    id = models.CharField(max_length=50,primary_key = True)
    date = models.CharField(max_length=50)
    price = models.FloatField()
    def __str__(self):
        return f"{self.id}"
    
    
class Order_Menu(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order,on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self + self.order}"  
    


class Reservation(models.Model):
    id = models.CharField(max_length=50,primary_key = True)
    date = models.CharField(max_length=50,)
    time = models.CharField(max_length=50,)
    no_of_customers = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.date + self.customer.first_name}"
    
class Delivery(models.Model):
    cat = [("On Going","On Going"),("Completed","Completed"),("Cancelled","Cancelled")]
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="delivers")
    category = models.CharField(max_length = 50)
    status = models.CharField(default =cat[0],choices = cat,max_length = 50)
    building_no = models.CharField(null= True,max_length=50)
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    zipcode = models.IntegerField()
    
    def address(self):
        return f"{self.building_no  +  self.street_name + self.city }"
    
    
class Transaction(models.Model):
    cat = [("Due","Due"),("Completed","Completed"),("Cancelled","Cancelled")]
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name = "transc")
    status = models.CharField(default =cat[0],choices = cat,max_length = 50)
    amount_paid = models.FloatField(default=0)
    price = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    # amount_paid = models.DecimalField(max_digits=5, decimal_places=2)
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # tax = models.DecimalField(decimal_places=2,max_digits=5)
    # discount = models.DecimalField(default=0,max_digits=5, decimal_places=2)
class Inventory(models.Model):
    name = models.CharField(max_length = 50)
    purchase_date = models.DateTimeField()
    stock_available = models.IntegerField()
    
class Shift(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    no_of_employees = models.IntegerField()
    startTime = models.CharField(max_length = 50)
    endTime = models.CharField(max_length = 50)
    day = models.CharField(max_length = 50)
    

class Works_in(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE)


class PlaceOrder(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="places")
    
class MakesFood(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    
class Use(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)

class Maintains_by(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    
class Makes_Delievery(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    

    
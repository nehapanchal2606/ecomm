from django.db import models
from account.models import *
import uuid
# # Create your models here.

color_choice = (('w', 'White'),
                ('b', 'black'),
                ('p', 'pink'),
                ('bl', 'blue'),
                ('y', 'yellow'),
                ('r', 'red'),
                ('o', 'orange'),
                ('pu', 'purple'),
                ('br', 'brown'),
                ('g', 'gray'),
                ('gr', 'green'),
                )


class sub_category(models.Model):
    sub_category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.sub_category_name


class product(models.Model):
    sub_category_id = models.ForeignKey(
        sub_category, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=250)
    price = models.IntegerField()
    color = models.CharField(max_length=20, choices=color_choice, default='w')
    image = models.FileField()
    description = models.TextField()
    size = models.CharField(max_length=150)


class wishlist(models.Model):
    product_id = models.ForeignKey(
        product, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)


class cart(models.Model):
    product_id = models.ForeignKey(
        product, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()


class order_details(models.Model):
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    date_oreder = models.DateField()
    complete = models.CharField(max_length=100)


class order_item(models.Model):
    product_id = models.ForeignKey(
        product, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(
        order_details, on_delete=models.CASCADE, null=True)
    date_added = models.DateField()
    quantity = models.IntegerField()


class checkout(models.Model):
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(
        order_details, on_delete=models.CASCADE, null=True)
    contact_no = models.CharField(max_length=13)
    total_amount = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=8)
    date_added = models.DateField()


class review(models.Model):
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(
        product, on_delete=models.CASCADE, null=True)
    description = models.TextField()


class payments(models.Model):
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
    timestamp = models.TimeField()


class contact_us(models.Model):
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    enquiry = models.TextField()


# class people(models.Model):
#     people_id = models.CharField(
#         max_length=30, primary_key=True, default=uuid.uuid4)
#     name = models.CharField(max_length=20, null=True)
#     link = models.CharField(max_length=20, null=True)


# class experience(models.Model):
#     exp_id = models.CharField(
#         max_length=30, primary_key=True, default=uuid.uuid4)
#     people_id = models.ForeignKey(people, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=250, null=True)
#     company_url = models.CharField(max_length=250, null=True)
#     designation = models.CharField(max_length=250, null=True)
#     yearofexp = models.CharField(max_length=250, null=True)
#     subdesigntion = models.CharField(max_length=250, null=True)
#     subyearofexp = models.CharField(max_length=250, null=True)


# class educcation(models.Model):
#     edu_id = models.CharField(
#         max_length=30, primary_key=True, default=uuid.uuid4)
#     people_id = models.ForeignKey(people, on_delete=models.CASCADE)
#     dname = models.CharField(max_length=250, null=True)
#     year = models.CharField(max_length=250, null=True)

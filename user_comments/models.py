from django.db import models

# Create your models here.

"""User model for storing user info"""
class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)

"""Comment model for storing comment info and associate the comment with user"""
class Comments(models.Model):
    title = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self,postData):
        errors= {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] =  "Invalid email address"
        if len(postData['password']) < 8:
            errors['password'] = "Password must have at least 8 characters"
        return errors
        


class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
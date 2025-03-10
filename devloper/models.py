from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore
from django.conf import settings # type: ignore
from django.core.validators import EmailValidator # type: ignore

class User(AbstractUser):
    email = models.EmailField(unique=True,null=True, blank=True )  
    username = models.CharField(max_length=150, unique=True,null=True, blank=True ) 
    password = models.CharField(max_length=128,null=True, blank=True)
    
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email
    
    
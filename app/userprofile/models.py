from django.db import models
from django.contrib.auth.models import User


class Userprofile(models.Model):
    '''
    Django user class has built in attributes username, first_name, last_name, email, password.
    Its also has method is_authenticated through which we can check whether the user is logged in.
    Refer to django documentation for more information https://docs.djangoproject.com/en/4.2/ref/contrib/auth/ 
    '''
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.username
    
    


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations= True

    def createuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError ('Email is required')
        email= self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
       # extra_fields.setdefault('*args:object',None)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be a staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have superuser true')
        return self.createuser(email, password, **extra_fields)

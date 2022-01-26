from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations= True

    def createuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError ('Email is required')
        email= self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('*args:object',None)
        if extra_field.get('is_staff') is not True:
            raise ValueError('superuser must be a staff')
        return self.createuser(email, password, **extra_field)

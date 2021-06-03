from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
  def create_user(self, email, name, password=None):
    """
    Creates and saves a User with the given email and password.
    """
    if not email:
      raise ValueError("Users must have an email address")

    email = self.normalize_email(email)
    user = self.model(email=email, name=name)

    user.set_password(password)
    user.save()
    return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
  """
  Creating my custom User
  """
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)  # a admin user; non super-user
  # notice the absence of a "Password field", that is built in.

  # hook in the New Manager to our Model
  objects = UserAccountManager()

  USERNAME_FIELD = 'email' # uniqe identifier
  REQUIRED_FIELDS = ['name'] # Email & Password are required by default

  def get_full_name(self):
    return self.name

  def get_short_name(self):
    return self.name

  def __str__(self):
    return self.email
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

    def create_staffuser(self, email, name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    Creating my custom User
    """
    email = models.EmailField(max_length=255, unique=True, )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # a admin user; non super-user
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that is built in.

    # hook in the New Manager to our Model
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'  # uniqe identifier
    REQUIRED_FIELDS = ['name']  # Email & Password are required by default

    def get_full_name(self):
        # The user is identified by their name
        return self.name

    def get_short_name(self):
        # The user is identified by their name
        return self.name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # User have specific permission
        return True

    def has_module_perms(self, app_label):
        # User have permissions to view the app
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

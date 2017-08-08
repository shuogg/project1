#! usr/bin/python 
#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from datetime import *
from tables import *


    


class UserManager(BaseUserManager):

    def create_user(self, name,  password=None):
	print 'username type:',type(name)


        user = self.model(
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name,  password=None):

        user = self.create_user(name,  password)
        user.is_admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    '''用户表'''
    AccountID = models.AutoField(primary_key=True,unique=True)      #账号ID
    name= models.CharField(max_length=11,unique=True,null=False)
    username = models.CharField(max_length=10,null=True)
    channel = models.IntegerField(null=True)
    from_id = models.CharField(max_length=11,null=True)
    token = models.CharField(max_length=20,null=True)
    time = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    expires_in = models.BigIntegerField(default=0)
	

    objects = UserManager()

    USERNAME_FIELD = 'name'
    #REQUIRED_FIELDS = ('name',)

    class Meta:
        ordering = ('AccountID',)

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return self.name


    def get_short_name(self):
        return self.name

    def get_id(self):
        return self.AccountID

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



class AbstractBaseUser(models.Model):
    password = models.CharField(('password'), max_length=128)

    is_active = True

    REQUIRED_FIELDS = []

    class Meta:
        abstract = True

    def get_username(self):
        "Return the identifying username for this User"
        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):
        return self.get_name()

    def natural_key(self):
        return (self.get_name(),)

    def is_anonymous(self):
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Sets a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        return is_password_usable(self.password)

    def get_full_name(self):
        raise NotImplementedError()

    def get_short_name(self):
        raise NotImplementedError()

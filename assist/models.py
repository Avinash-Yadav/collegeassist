from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User,update_last_login,PermissionsMixin , Group
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user( self, email, password,user_role, is_active, is_admin, **extra_fields):
        now=timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, user_role = user_role, is_admin=is_admin, is_active=is_active, last_login=now,**extra_fields)
        user.set_password(password)
        user.is_superuser =is_admin
        user.save()
        if user_role == 'super' :
            g = Group.objects.get(name='super_group')
            user.groups.add(g) #print(.groups)
        elif user_role =='student':
            g = Group.objects.get(name = 'student_group')
            print(g.permissions)
            user.groups.add(g) #print(customer.groups)
        else:
            g = Group.objects.get(name = 'instructor_group')
            print(g.permissions)
            user.groups.add(g)
			#print(customer.groups)
            return user
    
    def create_user(self, email,user_role,password=None,**extra_fields):
        return self._create_user(email,password,user_role,True,False,**extra_fields)
    
    def create_superuser(self, email,user_role,password=None,**extra_fields):
        return self._create_user(email,password,'super',True,True,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email           = models.EmailField(_('email address'), unique=True)
    first_name      = models.CharField(_('first name'), max_length=30, blank=True)
    last_name       = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined     = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active       = models.BooleanField(_('active'), default=True)
    is_admin 		= models.BooleanField(default=False)
    avatar          = models.ImageField(upload_to='static/avatars/', null=True, blank=True)
    user_role	    = models.CharField(max_length=8,choices=(('student','student'),('instructor','instructor'),('super','super')),default='student')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_role']

    class Meta:
        # pass
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return self.email

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return perm in self.get_all_permissions()
    
    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
    def is_staff(self):
        return self.is_admin
    
    def get_groups(self):
        groups = ''
        for i in self.groups():
            groups += i+', '
        return groups

class Student(models.Model):
    user = models.OnetoOneField('User')
    registration_no = models.CharField(max_length=20,blank=True,null=True)
    semester = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(8)])

    def __str__(self):
        return self.registration_no
    

class Department(models.Model):
    name    = models.CharField(max_length = 50,blank=False,null=False)
    acronym = models.CharField(max_length=10,blank=False,null=False)
    
    def __str__(self):
        return self.acronym
        
class Course(models.Model):
    name    = models.CharField(max_length=50,blank=False,null=False)
    dept    = models.ForeignKey('Department')
    code    = models.CharField(max_length=10,blank=False,null=False,unique=True)
    
    def __str__(self):
        return self.name
        

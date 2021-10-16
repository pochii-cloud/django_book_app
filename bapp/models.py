from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .utils import CustomUserManager
import uuid
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils.text import slugify
import string  # for string constants
import random  # for generating random strings


# img,url,faq are linked to book model
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    membership = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.email


class book_list(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                               editable=True)  # set editable to false later in production
    book_title = models.CharField(max_length=100, blank=False)
    book_code = models.CharField(max_length=100, blank=True)
    book_img = models.ImageField(verbose_name='book Image', upload_to="book_img", blank=True, )
    book_description = RichTextField(blank=True, null=True)
    status_choices = (

        ('Active', 'Active'),
        ('Inactive', 'Inactive'),

    )
    PUBLISH_STATUS = (
        ('Pending', 'Pending'),
        ('Published', 'Published'),
    )
    subscription_status = models.CharField(
        choices=status_choices, default='Pending', max_length=40)

    subscription_id = models.CharField(verbose_name='subscription ID', max_length=100, blank=False)
    book_plan = models.CharField(max_length=10, null=False)
    book_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    publishing_status = models.CharField(choices=PUBLISH_STATUS, max_length=15, default="Pending", null=False)
    creation_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=False, blank=True, max_length=250)

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        return super().save(*args, **kwargs)

    def generate_slug(self, save_to_obj=False, add_random_suffix=True):

        generated_slug = slugify(self.book_title)

        # Generate random suffix here.
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])

        return generated_slug

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return str(self.book_title)

    def get_absolute_url(self):
        return reverse('bapp:viewbook',
                       args=[str(self.id)])

    def __str__(self):
        return self.book_title


class img_addon(models.Model):
    id = models.AutoField(primary_key=True)
    img_title = models.CharField(max_length=100, blank=False)
    book = models.ForeignKey(book_list, on_delete=models.CASCADE, blank=False, null=True)
    img = models.ImageField(verbose_name='book Image', upload_to="book_img", blank=True, )

    def __str__(self):
        return self.img_title


class chapter(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    order = models.PositiveIntegerField(default=0)
    chapter_title = models.CharField(max_length=100, blank=False)
    chapter_body = RichTextField(blank=True, null=True)
    chapter_rank = models.PositiveSmallIntegerField(verbose_name="Rank", default=0)
    chapter_file = models.FileField(blank=True, null=True)
    book = models.ForeignKey(book_list, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.chapter_title


class services(models.Model):
    id = models.AutoField(primary_key=True)
    service_title = models.CharField(max_length=100, blank=False)
    service_img = models.ImageField(verbose_name='service Image', upload_to="service_img", blank=True, )
    service_short_description = RichTextField(blank=True, null=True)
    service_point1 = RichTextField(blank=True, null=True)
    service_point2 = RichTextField(blank=True, null=True)
    service_point3 = RichTextField(blank=True, null=True)
    service_point4 = RichTextField(blank=True, null=True)

    service_fee = models.PositiveSmallIntegerField(verbose_name="Service fee", default=0)
    service_user = models.ForeignKey(User, on_delete=models.CASCADE)

    slug = models.SlugField(unique=False, blank=True, max_length=250)

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        return super().save(*args, **kwargs)

    def generate_slug(self, save_to_obj=False, add_random_suffix=True):

        generated_slug = slugify(self.service_title)

        # Generate random suffix here.
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])

        return generated_slug

    class Meta:
        ordering = ('-service_title',)

    def __str__(self):
        return str(self.service_title)

    def get_absolute_url(self):
        return reverse('bapp:viewservice',
                       args=[str(self.id)])


class servicesubscription(models.Model):
    sub_id = models.CharField(
        verbose_name="Subscription ID ", max_length=100, blank=False)
    txn_date = models.DateTimeField(blank=True)
    exp_date = models.DateTimeField(blank=True)
    txn_id = models.CharField(
        verbose_name="Invoice ID", max_length=100, blank=False)
    service_id = models.OneToOneField(services, null=True, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['txn_date']

    def __str__(self):
        return self.sub_id

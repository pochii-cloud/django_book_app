from django.contrib.auth.forms import UserCreationForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from .models import  *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email',  'password1', 'password2']

class UpdatePassword(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user']


# class UpdateCouponForm(ModelForm):
#     class Meta:
#         model = Book_list
        
#         fields = ['book_title', 'book_code', 'book_img', 'book_description',
#                     'subscription_status', 'subscription_id', 'publishing_status', 'publishing_status']

# class UpdatePropertyForm(ModelForm):
#     class Meta:
#         model = Book_list
        
#         fields = ['Book_name', 'Book_headline', 'Book_image', 'Book_description',
#                     'Book_special_description', 'Book_link', 'publishing_status']
        

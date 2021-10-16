from bapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .forms import *


def login_view(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('bapp:dashboard_usr')
    else:
        if request.method == 'POST':
            if request.POST.get('submit') == 'sign_in':
                email = request.POST.get('email')
                password = request.POST.get('password')

                user = authenticate(request, username=email, password=password)
                if user:
                    if user.is_active:
                        print(request.user)
                        login(request, user)
                        return redirect('bapp:homeview')

                    else:
                        messages.info(request, 'Verify your mail to get fullaccess !')
                        return redirect('bapp:login')
                else:
                    messages.error(request, 'Email or Password are incorrect')
                    return redirect('bapp:login')

            else:
                return render(request, 'bapp/user/login.html')
        else:
            return render(request, 'bapp/user/login.html')


# 10. Signup


def log_usr(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('bapp:homeview')
    else:
        if request.method == 'POST':
            if request.POST.get('submit') == 'sign_in':
                email = request.POST.get('email')
                password = request.POST.get('password')

                user = authenticate(request, username=email, password=password)
                if user:
                    if user.is_active:
                        print(request.user)
                        login(request, user)
                        return redirect('bapp:dashboard_usr')

                    else:
                        messages.info(request, 'Verify your mail to get fullaccess !')
                        return redirect('bapp:login')
                else:
                    messages.error(request, 'Email or Password are incorrect')
                    return redirect('bapp:auth')


            else:
                messages.error(request, "Something went wrong, Please try again!")
                return redirect("bapp:auth")

        context = {
            'form': form,

        }
        return render(request, 'bapp/user/authentication-signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('bapp:login')


@login_required
def viewbook(request, slug=None):
    book_instance = get_object_or_404(book_list, slug=slug)
    current_user = request.user
    chapters = chapter.objects.filter(book=book_instance).order_by('order')
    images = img_addon.objects.filter(book=book_instance)

    context = {
        'book': book_instance,
        'chapters': chapters,
        'images': images,
        'user': current_user,
        'slug': slug
    }
    return render(request, 'bapp/user/bookview.html', context)


def addchapter(request, slug):
    Chapter = chapter.objects.all()
    if request.POST:
        chapter_title = request.POST.get('chapter_title')
        mydescription = request.POST.get('mydescription')
        Chapter = chapter()
        Chapter.chapter_title = chapter_title
        Chapter.chapter_body = mydescription
        Chapter.book = book_list.objects.get(slug=slug)
        Chapter.save()
    return render(request, 'bapp/user/bookview.html', {'Chapter': Chapter, 'slug': slug})


def editbook(request, slug):
    if request.POST:
        book_title = request.POST.get('book_title')
        book_description = request.POST.get('book_description')
        publishing_status = request.POST.get('publishing_status')
        subscription = request.POST.get('subscription')
        book = book_list.objects.get(slug=slug)
        book.book_title = book_title
        book.book_description = book_description
        book.publishing_status = publishing_status
        book.subscription_status = subscription
        book.save()
    return redirect('/')


def file_upload_view(request):
    import pdb
    pdb.set_trace()
    if request.POST:
        chapter_file = request.FILES.get('file')
        book_list.objects.create(upload=chapter_file)
    return HttpResponse('upload')


@login_required()
def dash(request):
    current_user = request.user
    book = book_list.objects.filter(book_owner=current_user)
    context = {
        'book': book,

    }

    return render(request, 'bapp/user/index.html', context)


def orderhistory(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/booklist.html', context)


def vieworder(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/booklist.html', context)


def cancelorder(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/booklist.html', context)


# when the subscription ended the book status should change to expired
def cancel_activeorder(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/booklist.html', context)


# order will be marked as cancelled -- particular book code will be marked as cancelled
def refund(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/booklist.html', context)


def refund_confirmation(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/booklist.html', context)


def booklist(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/booklist.html', context)


def addbook(request):
    book = book_list.objects.all()

    context = {
        'book': book,

    }

    return render(request, 'bapp/user/addbook.html', context)


def servicelist(request):
    service_list = services.objects.all()

    context = {
        'services': service_list,
    }
    return render(request, 'bapp/user/services.html', context)


def myservices(request, ):
    current_user = request.user
    user_name = User.objects.get(email=current_user.email)
    service_list = services.objects.filter(service_user=user_name)

    context = {
        'services': service_list,
    }
    return render(request, 'bapp/user/myservices.html', context)


def viewservice(request, slug=None):
    service_list = services.objects.all()
    service_instance = get_object_or_404(service_list, slug=slug)
    current_user = request.user

    context = {
        'Service': service_instance,
        'user': current_user
    }
    return render(request, 'bapp/user/viewservice.html', context)


def serviceconfirmation(request, slug=None):
    service_list = services.objects.all()
    service_instance = get_object_or_404(service_list, slug=slug)
    current_user = request.user

    context = {
        'service': service_instance,
        'user': current_user
    }
    return render(request, 'bapp/user/serviceconfirmation.html', context)


def serviceordersuccess(request, ):
    service_list = services.objects.all()
    current_user = request.user

    context = {
        'user': current_user
    }
    return render(request, 'bapp/user/serviceorderconfirmation.html', context)


def changeorder(request):
    chapter_list = request.GET.getlist('chapter_list[]')
    for counter, chapter_id in enumerate(chapter_list):
        chapter_obj = chapter.objects.get(id=chapter_id)
        chapter_obj.order = counter + 1
        chapter_obj.save()

    return JsonResponse(data={'message':'success'}, safe=True)

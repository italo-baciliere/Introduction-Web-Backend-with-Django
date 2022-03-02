from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):

    features = Feature.objects.all()

    # feature0 = Feature()
    # feature0.id = 0
    # feature0.name = 'Lorem Ipsum'
    # feature0.details = 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi'
    # feature0.is_true = True
    # feature1 = Feature()
    # feature1.id = 1
    # feature1.name = 'Fast'
    # feature1.details = 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore'
    # feature1.is_true = True
    # feature2 = Feature()
    # feature2.id = 2
    # feature2.name = 'Magni Dolores'
    # feature2.details = 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia'
    # feature2.is_true = True
    # feature3 = Feature()
    # feature3.id = 3
    # feature3.name = 'Nemo Enim'
    # feature3.details = 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis'
    # feature3.is_true = True
    # features.append(feature0)
    # features.append(feature1)
    # features.append(feature2)
    # features.append(feature3)

    return render(request, 'index.html', {'features': features})
    # context = {
    #     'name': 'Ítalo Baciliere',
    #     'age': 23,
    #     'nationality': 'Brasilian'
    # }
    # return render(request, 'first_page.html', context)

def counter(request):
    words = request.POST['text']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            return redirect('login')

    else:
        return render(request, 'register.html')
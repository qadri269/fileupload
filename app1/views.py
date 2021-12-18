from django.shortcuts import render, redirect

from app1.forms import myform
from django.contrib import messages

# Create your views here.


def home(request):
    form = myform()
    if request.method == "POST":
        form = myform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'data is sent successfully')
            return redirect('/')

    context = {'form': form}
    return render(request, 'home.html', context)

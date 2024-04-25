from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_list(request):
    context = {'user_list' :User.objects.all()}  # Pass the user_list to the context
    return render(request, "Resource_Library_Register/user_list.html", context)

def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, "Resource_Library_Register/user_form.html", {'form': form})
    elif request.method == "POST":  # Make sure it's POST method
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to user list upon successful form submission
    return render(request, "Resource_Library_Register/user_form.html", {'form': form})

def user_delete(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/user/list')

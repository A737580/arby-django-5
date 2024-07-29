from django.shortcuts import render, redirect
from  django.contrib.auth import login, logout
from .forms import NewUserForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('myapp:index')
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:index')

    form = NewUserForm()
    context = {'form': form}
    return render(request, 'users/register.html',context)
# Create your views here.

@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image)
        profile.save()
    return render(request,'users/profile.htm')
def seller_profile(request,id):
    seller = User.objects.get(id=id)
    context = {'seller':seller}
    return render(request,'users/sellerprofile.html', context)




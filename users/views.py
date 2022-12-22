from django.shortcuts import render
from .forms import UserForm, RawUserForm
from .models import User

def user_details_view(request):
    obj = User.objects.get(id=1)
    context = {
        'first_name': obj.first_name,
        'last_name': obj.last_name,
        'object': obj
    }
    return render(request, "users/users_details.html", context)

# def user_new_view(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {
#         'form': form
#     }
#     return render(request, "users/users_another_details.html", context)
def user_new_view(request):
    my_form = RawUserForm()
    if request.method == "POST":
        my_form = RawUserForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            User.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    # new_first_name = request.POST.get('first_name')
    # print(new_first_name)
    # context = {}
    return render(request, "users/users_another_details.html", context)

# Create your views here.

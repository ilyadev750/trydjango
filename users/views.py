from django.shortcuts import render
from .models import User

def user_details_view(request):
    obj = User.objects.get(id=1)
    context = {
        'first_name': obj.first_name,
        'last_name': obj.last_name,
        'object': obj
    }
    return render(request, "details.html", context)
# Create your views here.

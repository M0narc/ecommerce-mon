from django.shortcuts import render
from .models import Usuario

# Create your views here.
def user_list(request):
    get_users = Usuario.objects.all()

    data = {
        'get_users': get_users
    }
    return render(request, 'userList.html', data)

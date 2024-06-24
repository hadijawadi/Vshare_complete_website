from django.shortcuts import render




def register_user(request):
    return render(request,'account_app/pages/register.html')

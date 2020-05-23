from django.shortcuts import render


# Create your views here.
def adminhp(request):
    return render(request, 'adminhp.html')

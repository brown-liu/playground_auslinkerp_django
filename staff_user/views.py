from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from staff_user.models import staff, hours
import datetime


def register(request):
    if request.method == 'GET':
        person = staff.objects.all()
        show_staff = person.values()
        data = {
            'title': 'Register',
            'h1title': "Staff Register page",
            'show_staff': show_staff
        }
        return render(request, 'register.html', context=data)

    elif request.method == "POST":

        newuser = staff()
        newuser.s_name = request.POST.get('username')
        newuser.s_mobilenumber = request.POST.get('mobile_number')

        try:

            newuser.save()

            return redirect(reverse('staff_user:register'))
        except Exception as e:
            return HttpResponse('{}'.format(str(e) + "Please go back"))


def login(request):
    return redirect(reverse('homepage'))


def removestaff(request):
    id_number = request.POST.get("id_number")
    person = staff.objects.filter(id=id_number)
    person.delete()
    # print(id_number)

    return redirect(reverse('staff_user:register'))


def worktime(request):
    try:
        person = staff.objects.filter(s_isworking=True)
        detail = person.values()
        if person.exists():
            print(person.exists)
            data = {'working': detail,
                    'h3title': 'Our team is working hard!'}
            return render(request, 'worktime.html', context=data)
        else:
            data = {'h3title': ' You must be the first one! Or the last one here!'}

            return render(request, 'worktime.html', context=data)
    except Exception as e:
        return HttpResponse(e)


# start and stop work

def work(request):
    try:

        number = request.POST.get('mobile_number')
        person = staff.objects.get(s_mobilenumber=number)
        staff_name = person.s_name

        if person.s_isworking == False:
            person.s_isworking = True
            data = {
                'message': "Great, Let's WORK",
                'staff_name': person.s_name,
                'notice': "Please Don't forget to log off at end of the day"
            }
            if hours.objects.filter(h_name=staff_name, record_date=datetime.date.today()).exists() == False:
                print("AAA")
                staff_hour = hours()
                staff_hour.h_name = staff_name
                staff_hour.save()

            else:
                pass

        elif person.s_isworking == True:
            person.s_isworking = False
            person_hour = hours.objects.get(h_name=staff_name, record_date=datetime.date.today())
            person_hour.end_time = datetime.datetime.now()
            # person_hour.hours_today = (person_hour.end_time - person_hour.start_time).seconds / 3600
            print(type(person_hour.end_time))
            print(person_hour.end_time)
            person_hour.save()

            data = {
                'message': "Have a good rest, See you",
                'staff_name': person.s_name,
            }

        person.save()

        return render(request, "thank you.html", context=data)
    except Exception as e:
        return HttpResponse("Wrong number entered. please make sure no space between numbers!" + str(e))

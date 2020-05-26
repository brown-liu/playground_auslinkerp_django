import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from staff_user.models import staff, hours
from datetime import datetime, date

from warehouse.models import carton_cloud_client, containers


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
    if request.method=="GET":

        try:
            company = carton_cloud_client.objects.filter(c_active=0)
            companylist = company.values()

            container = containers.objects.all()
            obj_dict = container.values()

            person = staff.objects.filter(s_isworking=True)
            detail = person.values()
            if person.exists():
                print(person.exists)
                data = {'working': detail,
                        "company": companylist,
                        'container': obj_dict,
                        'h3title': 'Our team is working hard!'}
                return render(request, 'worktime.html', context=data)
            else:
                data = {'h3title': ' You must be the first one! Or the last one here!'}

                return render(request, 'worktime.html', context=data)
        except Exception as e:
            return HttpResponse(e)


# start and stop work

def work(request):

    number = request.POST.get('mobile_number')
    person = staff.objects.get(s_mobilenumber=number)
    staff_name = person.s_name

    if person.s_isworking == False:
        person.s_isworking = True
        data = {
            'message': "Great, Let's WORK",
            'staff_name': person.s_name,
            'notice': "Please Don't forget to log off when leave work!"
        }
        if hours.objects.filter(h_name=staff_name, record_date=date.today()).exists() == False:

            staff_hour = hours()
            staff_hour.h_name = staff_name
            staff_hour.save()

        else:
            pass

    elif person.s_isworking == True:
        person.s_isworking = False
        person_hour = hours.objects.get(h_name=staff_name, record_date=date.today())
        endtime = datetime.now()
        person_hour.end_time = str(endtime)
        person_hour.save()
        str_starttime = person_hour.start_time
        starttime = datetime.strptime(str_starttime, "%Y-%m-%d %H:%M:%S.%f")


        person_hour.hours_today = endtime - starttime
        person_hour.save()

        data = {
            'message': "Have a good rest, See you",
            'staff_name': person.s_name,
        }

    person.save()

    return render(request, "thank you.html", context=data)


# except Exception as e:
# return HttpResponse("Wrong number entered. please make sure no space between numbers!" + str(e))

# end time=2020-05-23 20:39:55.555596
# starttime=20:19:20.640904
# return int
# def timedifference(str_endtime,str_starttime):
#     str1=str_starttime
#     x=str1.split(':')
#     xH=int(x[0])
#     xM=int(x[1])
#     str2 = str_endtime
#     y = str2.split(' ')
#     y1 = y[1].split(':')
#     yH = int(y1[0])
#     yM = int(y1[1])
#
#     if yM>xM:
#         int_H=yH-xH
#         m_diff=yM-xM
#     else:
#         m_diff = yM + 60 - xM
#         int_H = yH - xH - 1
#
#     int_M=m_diff/60
#     return (int_H+int_M)
#
def staff_information(request):
    staff_all = staff.objects.all()
    staff_all_values = staff_all.values()

    staff_onduty = staff.objects.filter(s_isworking=1)
    staff_onduty_values = staff_onduty.values()

    staff_hour = hours.objects.all()
    staff_hour_values = staff_hour.values()

    data = {
        'stafflist': staff_all_values,
        'staff_onduty': staff_onduty_values,
        'hours': staff_hour_values

    }
    return render(request, 'staff_information.html', context=data)

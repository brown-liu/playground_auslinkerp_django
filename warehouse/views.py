from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from warehouse.models import containers, carton_cloud_client, location_used
import ast


def whhp(request):
    container = containers.objects.all()
    obj_dict = container.values()
    context = {
        'container': obj_dict
    }
    return render(request, 'whhp.html', context=context)


def container_upload_info(request):
    if request.method == 'POST':
        print(request.POST)
        obj_container = request.POST
        container = containers(ctnr_number=obj_container['ctnr_number'], ctnr_type=obj_container['ctnr_type'], \
                               ctnr_eta=obj_container['ctnr_eta'], \
                               ctnr_owner=obj_container['ctnr_owner'], ctnr_job=obj_container['ctnr_job'])
        container.save()
        return render(request, 'whhp.html')

    elif request.method == "GET":

        return render(request, 'whhp.html')
    else:
        return HttpResponse("Something Wrong")


def containerregister(request):
    if carton_cloud_client.objects.all().exists():
        container_owner = carton_cloud_client.objects.all().order_by('c_name')
        names = container_owner.values()

        container = containers.objects.all()
        detail = container.values()

        context = {
            "container": detail,
            'container_client': names
        }


        return render(request, 'containerregister.html', context=context)
    else:
        return render(request, 'containerregister.html')


def warehouseinfo(request):
    # 查找最新的记录 last（）
    if request.method == "GET":
        current_location = location_used.objects.all().last()

        if current_location != None:
            current_location_string = current_location.l_details
            # print(current_location_string)
            current_location_dict = ast.literal_eval(current_location_string)

            # 遍历所有记录 找出所有时间点 这个是给下拉 显示的时间戳
            all_location = location_used.objects.all()
            all_time_stamp = all_location.values()

            xdata = []
            ydata = []
            for i in current_location_dict:
                # print(i+'<==this is I')
                xdata.append(i)
                ydata.append(current_location_dict[i])
            # 这个是给label 显示的时间戳
            time_stamp = current_location.l_time

            xdata.append('Empty Location')

            empty_location = location_calc(ydata)
            ydata.append(empty_location)

            chartdata = {'x': xdata, 'y': ydata}
            charttype = "pieChart"
            chartcontainer = 'piechart_container'
            data = {
                'timestamp': time_stamp,
                'current_location_dict': current_location_dict,
                'charttype': charttype,
                'chartdata': chartdata,
                'all_time_stamp': all_time_stamp,
                'chartcontainer': chartcontainer,
                'empty_location': empty_location,
                'extra': {
                    'x_is_date': False,
                    'x_axis_format': '',
                    'tag_script_js': True,
                    'jquery_on_ready': False,
                }
            }
            return render(request,'warehouseinfo.html', data)
        else:
            return HttpResponse('No infor yet')
    elif request.method == "POST":
        pass


# East tamaki warehouse total pallets 594  16/05/2020
def location_calc(input_list):
    sum = 0
    for i in input_list:
        sum += i
    result = 594 - sum
    return result


def weeklychecksheet(request):
    return render(request, 'weeklychecksheet.html')


def update_timestap(request):
    temp = request.POST
    for newdate in temp:
        n = json.loads(newdate)

    update_timestamp = n["B"]
    display_timestamp = n["A"]
    print(update_timestamp)

    new_date = datetime.strptime(update_timestamp, '%Y-%m-%d')

    date = datetime.strptime(display_timestamp, '%b %d, %Y')

    checkpoint = location_used.objects.get(l_time=date)
    checkpoint.l_time = new_date
    checkpoint.save()
    return HttpResponse('OK')


def update_chart(request):
    item = request.POST.get("display")

    date = datetime.strptime(item, '%b %d, %Y')

    if location_used.objects.filter(l_time=date).exists():
        current_location = location_used.objects.get(l_time=date)
    else:
        current_location = location_used.objects.last()

    current_location_string = current_location.l_details

    current_location_dict = ast.literal_eval(current_location_string)

    # 遍历所有记录 找出所有时间点 这个是给下拉 显示的时间戳
    all_location = location_used.objects.all()
    all_time_stamp = all_location.values()

    xdata = []
    ydata = []
    for i in current_location_dict:
        # print(i+'<==this is I')
        xdata.append(i)
        ydata.append(current_location_dict[i])
        # 这个是给label 显示的时间戳
    time_stamp = current_location.l_time

    xdata.append('Empty Location')

    empty_location = location_calc(ydata)
    ydata.append(empty_location)

    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'timestamp': time_stamp,
        'current_location_dict': current_location_dict,
        'charttype': charttype,
        'chartdata': chartdata,
        'all_time_stamp': all_time_stamp,
        'chartcontainer': chartcontainer,
        'empty_location': empty_location,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }

    return render(request, 'warehouseinfo.html', context=data)


def change_container_status(request):
    if request.method == "GET":
        container = containers.objects.all()
        detail = container.values()
        data = {
            "container": detail,
        }

        return render(request, "containerregisterpage", context=data)


def container_detail_ajax(request):
    receive = request.POST.get("key")
    container = containers.objects.get(ctnr_number=receive)
    eta = str(container.ctnr_eta)
    # response_data={}
    # response_data['a']=eta

    data = {
        'a': eta,
        'b': container.ctnr_job,
        'c': container.ctnr_owner,
        'd': container.ctnr_type,
        'e': container.ctnr_active

    }

    return JsonResponse(data, safe=False)


def mark_job_done(request):
    container_number = request.POST.get("container_number")
    container = containers.objects.get(ctnr_number=container_number)
    print(container_number)
    container.ctnr_active = '0'
    container.save()

    return HttpResponse("GOOD")

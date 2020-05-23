from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from warehouse.models import containers, carton_cloud_client, location_used
import ast


def whhp(request):
    container = containers.objects.all()
    obj_dict = container.values()
    print(obj_dict)
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
                               ctnr_owner=obj_container['ctnr_owner'], ctnr_job=obj_container['ctnr_job'] \
                               , ctnr_special=obj_container['ctnr_special'])
        container.save()
        return render(request, 'whhp.html')

    elif request.method == "GET":

        return render(request, 'whhp.html')
    else:
        return HttpResponse("Something Wrong")


def containerregister(request):
    container_owner = carton_cloud_client.objects.all()
    names = container_owner.values()

    context = {
        'container_client': names
    }

    return render(request, 'containerregister.html')  # ,context=context


def warehouseinfo(request):
    # 查找最新的记录 last（）
    current_location = location_used.objects.all().last()
    current_location_string = current_location.l_details
    # print(current_location_string)
    current_location_dict = ast.literal_eval(current_location_string)

    # 遍历所有记录 找出所有时间点 这个是给下拉 显示的时间戳
    all_location = location_used.objects.all()
    all_time_stamp = all_location.values()
    print(all_time_stamp)
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
    return render_to_response('warehouseinfo.html', data)


# East tamaki warehouse total pallets 594  16/05/2020
def location_calc(input_list):
    sum = 0
    for i in input_list:
        sum += i
    result = 594 - sum
    return result


def weeklychecksheet(request):
    return render(request, 'weeklychecksheet.html')

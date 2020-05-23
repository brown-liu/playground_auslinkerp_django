from django.shortcuts import render
from warehouse.models import carton_cloud_client
from warehouse.models import containers


def homepage(request):
    company = carton_cloud_client.objects.filter(c_active=0)
    companylist = company.values()

    container = containers.objects.all()
    obj_dict = container.values()
    print(obj_dict)

    context = {
        "company": companylist,
        'container': obj_dict
    }
    return render(request, 'homepage.html', context=context)


def fangyuanguanli(request):
    return render(request, 'house_list.html')


def setCompanyStatus(request):
    company = carton_cloud_client.objects.all()
    companylist = company.values()
    company = carton_cloud_client.objects.filter(c_active=0)
    company_ishold = company.values()

    context = {
        "company": companylist,
        "company_ishold": company_ishold
    }

    return render(request, "setcompanystatus.html", context=context)


# 接收POST请求数据
def search_post(request):
    company = carton_cloud_client.objects.all()
    companylist = company.values()

    result = carton_cloud_client.objects.filter(c_name=request.GET['ClientSelected'])
    target = result.values()
    context = {
        "result": target,
        "company": companylist
    }

    return render(request, "setcompanystatus.html", context=context)


def clientDataEntry(request):
    return render(request, 'clientdataentry.html')


def successPage(request):
    return render(request, 'success.html')

    # else:
    # return HttpResponse("Missing Fields")


def change_onhold_status(request):
    client_temp = request.POST['company name']
    suspend_client = carton_cloud_client.objects.get(c_name=client_temp)

    if suspend_client.c_active == str(1):
        suspend_client.c_active = 0
        message = 'service on hold starts!'
        suspend_client.save()
        print('AA')
    else:
        suspend_client.c_active = 1
        suspend_client.save()
        message = 'service restriction removed! '
    context = {
        'suspend_client': suspend_client,
        'message': message
    }

    return render(request, 'homepage.html', context=context)


def weeklychecksheet(request):
    return render(request, 'weeklychecksheet.html')

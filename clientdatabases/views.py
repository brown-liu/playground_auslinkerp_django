from pandas import read_csv
from django.core.checks import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from warehouse.models import carton_cloud_client, location_used
from app.models import Clients


def clientdatabases(request):
    return render(request, 'client_on_hold')


# 转页面 带值显示
def change_onhold_status(request):
    if request.method == 'GET':
        # print('*'*10+str(request.GET))
        company = Clients.objects.all()
        companylist = company.values()
        context = {
            "company": companylist
        }

    return render(request, 'setcompanystatus.html', context=context)


# 转 页面
def quicklink(request):
    return render(request, 'quicklink.html')


# 转页面
def importafile(request):
    return render(request, 'importafile.html')


# 上传 cartoncloud导出的 客户名单
def uploadfile(request):  #
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        if not uploaded_file.name.endswith('.csv'):
            messages.ERROR(request, 'File is not CSV type')
            return HttpResponse("Failed")

        else:
            csv_file = uploaded_file.read().decode('utf-8')
            lines = csv_file.split("\n")
            for line in lines:
                item = line.split(',')
                print(item)
                new_client = carton_cloud_client(
                    c_id=item[0].strip('"'),
                    c_name=item[1].strip('"'),
                    c_email=item[2].strip('"'),
                    c_telephone=item[3].strip('"'),
                    c_customer_charge_name=item[4].strip('"'),
                    c_active=item[5].strip('"'))
                new_client.save()

            return render(request, 'success.html')


# 导入customer stock report 使用默认+location 模板 去头 pandas去重
def uploadfile_customer_stock(request):  #
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        if not uploaded_file.name.endswith('.csv'):
            messages.ERROR(request, 'File is not CSV type')
            return HttpResponse("Failed")

        else:
            csv_file = read_csv(uploaded_file, encoding='unicode_escape')
            # pandas去重
            csv_file = csv_file.drop_duplicates(subset=['Customer', 'Location'], keep='first')
            # pandas抓取同意客户的托盘数
            data_sorting = csv_file.set_index(['Customer', 'Code']).count(level='Customer')
            # pandas dataframe 转字典格式
            dict_file = data_sorting.to_dict()['Location']
            new_entry = location_used(l_details=dict_file)
            new_entry.save()
            return render(request, 'success.html')


def clientdbhp(request):
    return render(request, 'clientdbhp.html')

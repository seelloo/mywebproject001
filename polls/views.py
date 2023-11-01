from django.shortcuts import render
from django.http import HttpResponse
import requests
import geocoder
import datetime as dat


# Create your views here.
from django.template import loader


def index(request):
    return HttpResponse("Hello,world.You're at the polls index.")


def toLogin_view(request):
    return render(request, 'login.html')


def Login_view(request):
    u = request.GET.get("user", "")
    p = request.GET.get("password", "")

    if u and p:
        return HttpResponse("登录成功！")
    else:
        return HttpResponse("登录失败！")


def tempera_here(request):
    location = geocoder.ip('me').latlng
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    tempera_block = requests.get(api_request).json()
    now = dat.datetime.now()
    hour = now.hour
    # print(type(hour))
    tempera_now = tempera_block['hourly']['temperature_2m'][hour]
    template=loader.get_template('temperature.html')
    context = {'tempera': tempera_now,'hour':hour}
    return HttpResponse(template.render(context, request))
    #Index.html以黄色波浪线高亮显示，因为它尚不存在。 将光标悬停在它上面并选择Create template index.html（创建模板index.html）。
    # return HttpResponse(f"It's {hour} o'clock now , Here it's {tempera_now} °C")  # 网页输出
    # return tempera_now #调试输出

# if __name__=='__main__':
#     pcreturn=tempera_here()
#     print('over')

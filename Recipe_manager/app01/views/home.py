from app01.utils.bootstrap import BootStrapModelForm

from django.shortcuts import render, redirect, HttpResponse
from app01 import models


class MenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.home
        fields = "__all__"
        # exclude = ["id"]


def meun_list(request, nid):
    queryset = models.home.objects.filter(id=nid)
    tools = int(request.POST.get("tools"))
    for star in queryset:
        Star = star.rate

    return render(request, 'sec_menu.html', {"queryset": queryset, "tools": tools})


def meun_list1(request, nid):
    queryset = models.cust_recipe.objects.filter(id=nid)
    tools = int(request.POST.get("toolss"))

    return render(request, 'sec_menu3.html', {"queryset": queryset, "tools": tools})


def meun_list2(request, nid):
    queryset = models.cust_recipe.objects.filter(id=nid)

    return render(request, 'sec_menu2.html', {"queryset": queryset})

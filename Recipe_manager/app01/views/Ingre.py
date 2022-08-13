from django.shortcuts import render, redirect
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm


""" for meat """


class MainMenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.meat
        fields = "__all__"


class MainMenuModelForm1(BootStrapModelForm):
    class Meta:
        model = models.meat1
        fields = "__all__"


def meat(request):
    queryset = models.meat.objects.all()
    queryset1 = models.meat1.objects.all()

    return render(request, 'Ingrem.html', {"queryset": queryset, "queryset1": queryset1})


def madd(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm(data=request.POST, files=request.FILES)

    if form.is_valid():
        form.save()
        return redirect('/Ingredientm/')

    return render(request, 'upload_form.html', {"form": form, "title": title})

def madd1(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm1()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm1(data=request.POST, files=request.FILES)

    if form.is_valid():
        form.save()
        return redirect('/Ingredientm/')

    return render(request, 'upload_form.html', {"form": form, "title": title})





""" for vegetable """


class MainMenuModelForm_veg(BootStrapModelForm):
    class Meta:
        model = models.vegetable
        fields = "__all__"


class MainMenuModelForm_veg1(BootStrapModelForm):
    class Meta:
        model = models.vegetable1
        fields = "__all__"


def veg(request):
    queryset = models.vegetable.objects.all()
    queryset1 = models.vegetable1.objects.all()

    return render(request, 'Ingrev.html', {"queryset": queryset, "queryset1": queryset1})


def vadd(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm_veg()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm_veg(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredientv/')
    return render(request, 'upload_form.html', {"form": form, "title": title})



def vadd1(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm_veg1()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm_veg1(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredientv/')
    return render(request, 'upload_form.html', {"form": form, "title": title})


""" for Auxiliary"""


class MainMenuModelForm_aux(BootStrapModelForm):
    class Meta:
        model = models.Auxiliary
        fields = "__all__"


class MainMenuModelForm_aux1(BootStrapModelForm):
    class Meta:
        model = models.Auxiliary1
        fields = "__all__"


class MainMenuModelForm_aux2(BootStrapModelForm):
    class Meta:
        model = models.Auxiliary2
        fields = "__all__"


def aux(request):
    queryset = models.Auxiliary.objects.all()
    queryset1 = models.Auxiliary1.objects.all()
    queryset2 = models.Auxiliary2.objects.all()

    return render(request, 'Ingrea.html', {"queryset": queryset, "queryset1": queryset1, "queryset2": queryset2})


def aadd(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm_aux()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm_aux(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredienta/')
    return render(request, 'upload_form.html', {"form": form, "title": title})




def aadd1(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm_aux1()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm_aux1(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredienta/')
    return render(request, 'upload_form.html', {"form": form, "title": title})




def aadd2(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm_aux2()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm_aux2(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredienta/')
    return render(request, 'upload_form.html', {"form": form, "title": title})

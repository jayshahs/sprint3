from django.conf import settings
from django.shortcuts import HttpResponse, render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template import loader
from django.template.loader import render_to_string

from app01 import models


def mail_page(request, nid):
    """ email page """

    queryset = models.cust_recipe.objects.filter(id=nid)

    return render(request, 'sec_menu1.html', {"queryset": queryset})


def sendmail(request):
    """ send email """


    other = request.POST.get("mmm")
    data = {'name': 'join'}
    html_content = render_to_string('sec_menu1.html', data)
    subject = 'This is for practice'
    recipient_list = other
    msg = EmailMessage(subject,  # 邮件主题
                       html_content,  # 邮件内容，直接使用html代码就行
                       settings.EMAIL_HOST_USER,  # 用于发送邮件的用户
                       [recipient_list]  # 接收邮件的用户列表
                       )
    msg.content_subtype = 'html'
    msg.send()
    return redirect('/main1/')





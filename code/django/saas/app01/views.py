from django.shortcuts import render, HttpResponse
from utils.tencent.sms import send_sms_single
import random

# Create your views here.
def send_sms(request):
    code = random.randrange(1000,9999)
    res = send_sms_single('17314893371',832736,[code,])
    print(res)
    return HttpResponse('发送成功')

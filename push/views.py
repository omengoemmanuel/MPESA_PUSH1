import requests
from django.shortcuts import render, HttpResponse

from .credentials import MpesaPpassword, MpesaAccessToken


# Create your views here.


def pay(request):
    return render(request, 'pay.html')


def stk(request):
    if request.method == 'POST':
        phone = request.POST['pno']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_access_token
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": MpesaPpassword.short_code,
            "Password": MpesaPpassword.decoded,
            "Timestamp": MpesaPpassword.pay_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": MpesaPpassword.short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Web Development",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse("success")

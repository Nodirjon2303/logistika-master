from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import requests

# Create your views here.



def CalculatorPageView(request):
    DATA=Country.objects.all()
    add_inform = AdditionalInformation.objects.first()
    if request.user.username == '':
        user = authenticate(request, username='user', password='userpass')
        print(user)
        if user:
            login(request, user=user)
    return render(request=request,template_name='index.html', context={"country":DATA, "addition": add_inform})

def CompanySendFunc(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        kg=(data['weight'])
        comp=Company.objects.all()

        country=data['country']


        if kg==15:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg15*koeffisent




                a ={
                    'logo': i.company_logo,
                    'type': i.company_type,
                    'name':i.company_name,

                    'time':i.days,
                    'price':narx}
                data.append(a)
        if kg==0.5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg05*koeffisent
                a ={'name':i.company_name,
                    'time':i.days,'price':narx,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    }
                data.append(a)
        if kg==1:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg1*koeffisent

                a ={'name':i.company_name,'time':i.days,'price':narx,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    }
                data.append(a)
        if kg==2:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg2
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==3:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg3
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==4:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg4
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==5:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg5
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==6:
            data=[]
            for i in comp:

                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg6
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==7:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg7
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==8:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=i.kg8*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==9:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg9
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==10:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg10
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==11:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg11
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==12:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg12
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==13:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg13
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==14:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg14
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==15:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg15
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==16:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg16
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==17:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg17
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==18:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg18
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==19:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg19
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if kg==20:
            data=[]
            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx=koeffisent*i.kg20
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if  20<kg<45:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if  44<kg<71:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if  70<kg<101:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if  100<kg<300:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        if  299<kg:
            data=[]

            for i in comp:
                index = Index.objects.get(country__country=country,company=i )
                koeffisent=index.index
                narx =i.kg_21_44 * kg*koeffisent
                a ={'name':i.company_name,
                    'logo': i.company_logo.url,
                    'type': i.company_type,
                    'time':i.days,'price':narx}
                data.append(a)
        return JsonResponse({'data': data})

    return render(request=request,template_name='index.html')


def Saqlash(request):
    if request.method == 'POST':
        addition = AdditionalInformation.objects.first()
        data = json.loads(request.body)
        first_name = data['fname']
        last_name = data['lname']
        phone = data['phone']
        email = data['email']
        message = data['message']
        country = data['country']
        length = data['length']
        width = data['width']
        height = data['height']
        weight = data['weight']
        company_name = data['company_name']
        company_price = data['company_price']
        text=f"firstname:{first_name}\nlast_name:{last_name}\nphone:{phone}\nemail: {email}\nmessage:{message}\ncountry:{country}\nlength:{length} sm\nwidth:{width} sm\nheight:{height} sm\nweight:{weight} kg\n{company_name}\n{company_price}"
        try:
            requests.post(
                f'https://api.telegram.org/bot5191254844:AAHjg0ocEF6eS9p8H_xL1cCfrEo6oKYX8HI/sendMessage?chat_id=-100{addition.channel_id}&text={text}')
        except Exception as e:
            pass





        save_data.objects.create(first_name=data['fname'],last_name=data['lname'],phone=data['phone'],
                                 email=data['email'],message=data['message'],country=data['country'],
                                 length=data['length'],width=data['width'],height=data['height'],weight=data['weight'],company_name=data['company_name'],company_price=data['company_price'])




        return JsonResponse({'data': 'ok'})



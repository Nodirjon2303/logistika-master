from django.shortcuts import render
from .models import Trend
# Create your views here.
def TrendPageView(request):
    data=Trend.objects.all()

    DATA=[]


    for i in data:

        a={
            'title':i.title,
            'text':i.description,
            'img':i.img.url,
        }

        DATA.append(a)




    return render(request=request,template_name='trend.html',context={'data':DATA})


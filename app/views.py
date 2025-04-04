from django.shortcuts import render
# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

def insert_topic(request):
    tn=input('Enter topic name ')
    TTO=Topic.objects.get_or_create(topic_name=tn)
    if TTO[1]:
        return HttpResponse(f'{tn} is created')
    else:
        return HttpResponse(f'{tn} is Already exists')
    
def insert_webpage(request):
    tn=input('Enter topic name ')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        na=input('enter name ')
        url=input('enter url ')
        em=input('enter email ')
        mo=input('enter mobile ')
        TO=LTO[0]
        TWO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=em,mobile=mo)
        if TWO[1]:
            return HttpResponse(f'{na} is created')
        else:
            return HttpResponse(f'{na} is already exits')
    else:
        return HttpResponse(f'{tn} topic name is not Available')

def insert_accessrecord(request):
    pk=input('enter PK of webpage ')
    TWO=Webpage.objects.filter(pk=pk)
    if TWO:
        da=input('enter Date ')
        au=input('enter Author ')
        TO=TWO[0]
        TAO=AccessRecord.objects.get_or_create(name=TO,date=da,author=au)
        if TAO[1]:
            return HttpResponse(f'{pk} is created')
        else:
            return HttpResponse(f'{pk} is already exists')
    else:
        return HttpResponse(f'{pk} name is not Available')
    
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='Cricket') # given condition satisfied
    QLWO=Webpage.objects.exclude(topic_name='Cricket') # given condition not satisfied and remains data retrive
    QLWO=Webpage.objects.all()[1::2] # slicing the data
    QLWO=Webpage.objects.all()[::-1] # reverse order data
    QLWO=Webpage.objects.order_by('name') # based on ASCI values retrive the data
    QLWO=Webpage.objects.order_by('-name') # data should be descending order based on ASCI values
    QLWO=Webpage.objects.order_by(Length('name')) # number of characters in name gives ascending order
    QLWO=Webpage.objects.order_by(Length('name').desc()) # number of characters in name gives descending order
    
    #  filed lookups 
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__startswith='a') # no case sensitive
    QLWO=Webpage.objects.filter(name__endswith='I')  #  no case sensitive 
    QLWO=Webpage.objects.filter(name__contains='a') # having specified char into specified str
    QLWO=Webpage.objects.filter(pk__range=(2,5))  # 2 to 5 rows
    QLWO=Webpage.objects.filter(email__isnull=True) # null value data display
    QLWO=Webpage.objects.filter(email__isnull=False) # not null values data display
    QLWO=Webpage.objects.filter(pk__in=(2,4,5)) # display 2,4&5
    QLWO=Webpage.objects.filter(name__regex=r'^A\w+') # case sensitive data 
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(topic_name='Cricket', url__endswith='in')


    d1={'QLWO':QLWO}
    return render(request,'display_webpage.html',d1)

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__day='28')
    QLAO=AccessRecord.objects.filter(date__month='5')
    QLAO=AccessRecord.objects.filter(date__year='1998')
    QLAO=AccessRecord.objects.filter(date__month__gt='4')
    QLAO=AccessRecord.objects.filter(date__month__gte='4')
    QLAO=AccessRecord.objects.filter(date__month__lt='5')
    QLAO=AccessRecord.objects.filter(date__month__lte='5')
    
    d2={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d2)

def update_webpage(request):
    # by using update method

    # Updating single row
    Webpage.objects.filter(name='Virat').update(email='viratbhai123@gmail.com')

    # Updating multiple rows
    Webpage.objects.filter(topic_name='Cricket').update(url='https://cricket.in')

    # Updating zero rows ---> Nothing
    Webpage.objects.filter(topic_name='Boxing').update(mobile='9876543210')

    # Updating foreign key data ---> Error --- data present in parent table should be not provided
    #Webpage.objects.filter(name='Arjun').update(topic_name='Boxing') 
    Webpage.objects.filter(name='Arjun').update(topic_name='Swimming') 
    
    # by using update_or_create method

    # Updating single row
    Webpage.objects.update_or_create(name='abd',defaults={'url':'https://abd21.in'})
    
    # Updating multiple rows  --> Error
    #Webpage.objects.update_or_create(name='Cricket',defaults={'url':'https://suneel21.in'})

    # Updating foreign key data ---> Error --> parent table object is not provided...
    #Webpage.objects.update_or_create(name='Hardhik',defaults={'topic_name':'Boxing'})
    SO=Topic.objects.get(topic_name='Swimming')
    # Webpage.objects.update_or_create(name='Virat',defaults={'topic_name':SO})
    Webpage.objects.update_or_create(name='Sachin',defaults={'topic_name':SO})
    
    # Updating zero rows ---> it will start create 
    # Webpage.objects.update_or_create(name='Sachin',defaults={'topic_name':SO})
    Webpage.objects.update_or_create(name='Sachin',defaults={'mobile':9489347822})

    QLWO=Webpage.objects.all()
    d1={'QLWO':QLWO}
    return render(request,'display_webpage.html',d1)

def delete_webpage(request):
    Webpage.objects.filter(name='Sachin').delete()
    QLWO=Webpage.objects.all()
    d1={'QLWO':QLWO}
    return render(request,'display_webpage.html',d1)

def insert_webpage_by_forms(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        mo=request.POST['mo']
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em,mobile=mo)
        QLWO=Webpage.objects.all()
        d1={'QLWO':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage_by_forms.html',d)

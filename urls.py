"""
URL configuration for ITRproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ITRproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myhome),
    path('about/',views.myabout),
    path('table/',views.mytable),
    path('order/',views.myorder),
    path('contact/',views.mycontact),
    path('menu/',views.mymenu),
    path('chef/',views.mychef),
    path('gallery/',views.mygallery),
    path('bread/',views.mybread),
    path('deserts/',views.mydesert),
    path('rice/',views.myrice),
    path('startup/',views.mystart),
    path('drinks/',views.mydrink),
    path('all/',views.myall),
    path('maincourse/',views.mymaincourse),
    path('confirm/',views.myconfirm),
    path('book/',views.mybook),
    path('cancel/',views.mycancel),
    path('remove/',views.myremove),
    path('msg/',views.mymsg),
    path('footer/',views.myfooter),
    path('privacy/',views.myprivacy),
    path('adminhome/',views.myadminhome),
    path('adminorder/',views.myadminorder),
    path('adminmenu/',views.myadminmenu),
    path('admincustomer/',views.myadmincustomer),
    path('adminsetting/',views.myadminsetting),
    path('userhome/',views.myuserhome),
    path('userorder/',views.myuserorder),
    path('messages/',views.mymessage),
    path('task/',views.mytask),
    path('base/',views.mybase),
    path('burger/',views.myburger),
    path('fries/',views.myfries),
    path('crinkle/',views.mycrinkle),
    path('curly/',views.mycurly),
    path('sujji/',views.mysujji),
    path('vadapav/',views.myvadapav),
    path('dalmakhani/',views.mydalmakhani),
    path('aloogobhi/',views.myaloogobhi),
    path('daltadka/',views.mydaltadka),
    path('shahipaneer/',views.myshahipaneer),
    path('butterchicken/',views.mybutterchicken),
    path('chanamasala/',views.mychanamasala),
    path('shevbhaji/',views.myshevbhaji),
    path('kaju/',views.mykaju),
    path('grilled/',views.mygrilled),
    path('roti/',views.myroti),
    path('paratha/',views.myparatha),
    path('tandori/',views.mytandori),
    path('naan/',views.mynaan),
    path('puri/',views.mypuri),
    path('makka/',views.mymakka),
    path('jeera/',views.myjeera),
    path('plane/',views.myplane),
    path('veg/',views.myveg),
    path('brown/',views.mybrown),
    path('soya/',views.mysoya),
    path('chicken/',views.mychicken),
    path('icecream/',views.myicecream),
    path('pudding/',views.mypudding),
    path('kulfi/',views.mykulfi),
    path('pastry/',views.mypastry),
    path('rasmalai/',views.myrasmalai),
    path('panipuri/',views.mypanipuri),
    path('gulabjamun/',views.mygulabjamun),
    path('donut/',views.mydonut),
    path('chicken/',views.mypanipuri),
    path('coffeemousee/',views.mycoffeemousee),
    path('coffee/',views.mycoffee),
    path('orange/',views.myorange),
    path('lassi/',views.mylassi),
    path('lemonade/',views.mylemonade),
    path('soda/',views.mysoda),
    path('cocktail/',views.mycocktail),
    path('user1/',views.userlogin),
    path('admin1/',views.adminlogin),
    path('register/',views.myregister),

    ]




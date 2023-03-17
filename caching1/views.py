from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.cache import cache
# per view cache
from django.views.decorators.cache import cache_page



# Create your views here.
class temp_1(TemplateView):
    template_name = 'home.html'

# @cache_page(30)
def view_cache(request):
    return render(request,'home.html')


'''low level cache'''

# def low_level_cache(request):
#     data = cache.get('city','uddhav',30)
#     if data is None:
#         cache.set('city','Ahmedabad',30)
#         data = cache.get('city')
#     return render(request,'home.html',{'data':data})

# def low_level_cache(request):
#     data = cache.get_or_set("city","palanpur",30)
#     return render(request,'home.html',{'data':data})

def low_level_cache(request):
    data = {'name':'Nilesh','Age':21}
    cache.set_many(data,30)
    info = cache.get_many(data)
    return render(request,'home.html',{'info':info})

def del_cache(request):
    cache.clear()
    return render(request,'home.html')
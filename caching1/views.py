from django.shortcuts import render
from django.views.generic import TemplateView
# per view cache
from django.views.decorators.cache import cache_page



# Create your views here.
class temp_1(TemplateView):
    template_name = 'home.html'

# @cache_page(30)
def view_cache(request):
    return render(request,'home.html')
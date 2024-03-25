from django.shortcuts import render
from django.conf import settings

from .business_log import read_from_file


# Create your views here.
def index(request):
    return render(request, 'index.html')


def word_list(request):
    orig, trans = read_from_file('./myapp/static/files/dictionary.txt')
    data = list(zip(orig, trans))
    context = {'data': data}
    return render(request, 'word_list.html', context=context)
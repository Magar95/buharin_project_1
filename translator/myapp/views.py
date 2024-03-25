from django.shortcuts import render, redirect
from django.conf import settings

from .business_log import read_from_file, add_to_file


# Create your views here.
def index(request):
    return render(request, 'index.html')


def words_list(request):
    filename = './myapp/static/files/dictionary.txt'
    orig, trans = read_from_file(filename)
    data = zip(orig, trans)
    context = {'data': data}
    return render(request, 'word_list.html', context=context)


def add_word(request):
    if request.method == 'POST':
        word1 = request.POST['word1']
        word2 = request.POST['word2']
        filename = './myapp/static/files/dictionary.txt'
        add_to_file(filename, word1, word2)
        return redirect('/words_list')

    return render(request, 'add_word.html')
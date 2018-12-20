from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(req):
    return render(req, 'home.htm')


def count(req):
    fulltext = req.GET['fulltext']
    word_list = fulltext.split()
    word_count_Dictionary = {}
    for word in word_list:
        if word in word_count_Dictionary:
            # increase
            word_count_Dictionary[word] += 1
        else:
            word_count_Dictionary[word] = 1
    sortedWords = sorted(word_count_Dictionary.items(),
                         key=operator.itemgetter(1), reverse=True)
    return render(req, 'count.htm', {'fulltext': fulltext, 'word_list': len(word_list), 'word_count_Dictionary': word_count_Dictionary, 'sortedwords': sortedWords})

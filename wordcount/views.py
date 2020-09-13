from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            #insert
            word_dictionary[word] = 1
    word_count = len(word_dictionary)
    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'word_count': word_count, 'sorted_words': sorted_words})

def about(request):
    return render(request, 'about.html')
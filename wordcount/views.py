# First web home page

from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def count(request):
    fulltext = request.GET["fulltext"]
    print("now count the words")
    wordlist = fulltext.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            #increase count for tht word
            worddict[word] += 1
        else:
            # add word to dict
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", { "fulltext":fulltext, "count":len(wordlist), "sortedwords": sortedwords })

def hub(request):
    return HttpResponse("<h1>WakeHub</h1>")

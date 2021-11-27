# created by me
from   django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''
#     <h1>Navigation Bar</h1>
#     <a href='https://www.facebook.com'>Facebook</a> <br>
#     <a href='https://www.twitter.com'>Twitter</a> <br>
#     <a href='https://www.instagram.com'>Instagram</a> <br>
#     <a href='https://www.youtube.com'>YouTube</a> <br>
#     <a href='https://www.github.com'>GitHub</a>
#     ''')

def index(request):
    
    return render(request, 'index.html')
    # return HttpResponse('''
    # <h1>Home</h1>
    # <a href='/removepunc'>Remove Punctuation</a> <br>
    # <a href='/capitalizefirst'>Capitalize First</a> <br>
    # <a href='/newlineremove'>New Line Remove</a> <br>
    # <a href='/spaceremove'>Space Remove</a> <br>
    # <a href='/charcount'>Character Count</a>
    # ''')

def removepunc(request):
    return render(request, 'removepunc.html')
    # return HttpResponse('''
    # <h1>Remove Punctuation</h1>
    # <a href='/'>Home</a>
    # ''')

def capitalizefirst(request):
    return render(request, 'capitalizefirst.html')
    # return HttpResponse('''
    # <h1>Capitalize First</h1>
    # <a href='/'>Home</a>
    # ''')

def newlineremove(request):
    return render(request, 'newlineremove.html')
    # return HttpResponse('''
    # <h1>New Line Remove</h1>
    # <a href='/'>Home</a>
    # ''')

def spaceremove(request):
    return render(request, 'spaceremove.html')
    # return HttpResponse('''
    # <h1>Space Remove</h1>
    # <a href='/'>Home</a>
    # ''')

def charcount(request):
    return render(request, 'charcount.html')
    # return HttpResponse('''
    # <h1>Character Count</h1>
    # <a href='/'>Home</a>
    # ''')
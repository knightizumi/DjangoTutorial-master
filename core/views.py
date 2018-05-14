from django.http import HttpResponse
from django.shortcuts import render


def root(request):
    s = '<h1>Hello World</h1>'
    return HttpResponse(s)

def hi(request,w):
    # w = request.GET.get('w')
    return HttpResponse(w)

# def hello(request,n1,n2):
#     # w = request.GET.get('w')
#     return HttpResponse('<h1>{}</h1>'.format(n1+n2))

def hello(request,n1,n2):
    s = n1 + n2
    return render(request,'test.html',{
        's':s
    })

def homework1(request, start, stop, base):
    numArray = []
    isReversed = False
    if start > stop:
        # x = start
        # start = stop
        # stop = x
        start, stop = stop, start
        isReversed = True

    rr = range(start,stop+1)
    if isReversed:
        rr = reversed(rr)

    if base == 1:
        for num in rr:
            if num%2 == 1:
                numArray.append(num)
    else:
        for num in rr:
            if num%2 == 0:
                numArray.append(num)

    return render(request,'r.html',{
        'numArray':numArray
    })

def tag_test(request):
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return render(request, 'tag_test.html', {
        'l': l
    })

















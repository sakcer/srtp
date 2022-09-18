from django.shortcuts import render

def test(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test.html', context)
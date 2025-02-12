from django.shortcuts import render
from django.http import request, HttpResponse
# Create your views here.
def test(request):
    return render(request, 'index.html', context={'hello':'there'})
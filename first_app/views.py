from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def first_app(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def success_page(request):
    # print("10" * 10)
    return HttpResponse("""
    <h4> Hey I am success page!!</h4>
    <p> Hello, I'm from multiple html tag </p>
    <button style="color:red"> hello </button>
    
    """)
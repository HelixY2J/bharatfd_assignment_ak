from django.shortcuts import render

# Create your views here.
def faq_page(request):
    return render(request, "base.html")
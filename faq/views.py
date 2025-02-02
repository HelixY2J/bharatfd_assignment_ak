from django.shortcuts import render
from .models import FAQ
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers

class faqSerializaer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id','question', 'answer', 'ques_hindi', 'ques_bengali']

class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')

        faqs = FAQ.objects.all()

        if lang == 'hi':
            faqs = faqs.filter(question_hi__isnull=False)  
        elif lang == 'bn':
            faqs = faqs.filter(question_bn__isnull=False)

        serializer = faqSerializaer(faqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def faq_page(request):
    return render(request, "child.html")


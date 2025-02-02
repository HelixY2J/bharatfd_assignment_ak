from django.shortcuts import render
from .models import FAQ
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.views import APIView
from rest_framework import serializers,viewsets
from django.core.cache import cache
from rest_framework.pagination import PageNumberPagination

def get_faqs_from_cache(lang):
    cached_faqs = cache.get(f'faqs_{lang}')
    if isinstance(cached_faqs, list):  
        return cached_faqs
    
    if isinstance(cached_faqs, str): 
        return json.loads(cached_faqs)
    
    return None

def set_faqs_to_cache(lang, faqs_data):
    cache.set(f'faqs_{lang}', json.dumps(faqs_data), timeout=3600*24)

class faqPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class faqSerializaer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id','question', 'answer', 'question_hi', 'question_bn']

class faqViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    pagination_class = faqPagination
    serializer_class = faqSerializaer

    def list(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        cached_faqs = get_faqs_from_cache(lang)

        if cached_faqs:
            faqs_data = cached_faqs
        else:
            if lang not in ['hi', 'bn']:
                lang = 'en'
                faqs = FAQ.objects.all().values(
                    'id',
                    'question',
                    'answer'
                )
            else:
                faqs = FAQ.objects.all().values(
                    'id',
                    f'question_{lang}',
                    'answer'
                )
            faqs_data = [
                {
                    'id': faq['id'],
                    'question': faq.get(f'question_{lang}')
                    if lang != 'en'
                    else faq['question'],
                    'answer': faq['answer'],
                }
                for faq in faqs
            ]
            set_faqs_to_cache(lang, faqs_data)

        page = self.paginate_queryset(faqs_data)
        if page is not None:
            return self.get_paginated_response(page)

        return Response(faqs_data)


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


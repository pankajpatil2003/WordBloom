from django.http import JsonResponse
from .models import *
from django.views.decorators.http import require_POST, require_GET
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from .languageDetails import languages

@csrf_exempt
@require_POST
def bulk_upload_words(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({'status': 'error', 'message': 'No file provided'})

        file = request.FILES['file']
        words = []

        for line in file:
            word = line.strip().decode('utf-8')  
            words.append(englishWords(words=word))

        # Bulk insert the objects
        englishWords.objects.bulk_create(words)

        return JsonResponse({'status': 'success', 'message': 'Words added to the database'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@csrf_exempt
@require_GET
def search_word(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        word = data['word'].lower()
        langCode = data['lang_code']
        language = languages.get(langCode)
        
        # Check the cache first
        cached_result = cache.get(word)
        if cached_result:
            return JsonResponse({'status': 'success', 'message': 'Word Found', 'data': cached_result})

        # Query the database if not in cache
        found_word = language.objects.filter(words=word).first()
        if found_word:
            cache.set(word, found_word.words, timeout=300)  # Cache for 5 minutes
            return JsonResponse({'status': 'success', 'message': 'Word Found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Word Not Found'})

from django.shortcuts import render
from home.models import Search
import requests

API_KEY = '1ddb7df62cbdc4e07f6ec75ca78e2960'
API = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&tags={}&format=json&nojsoncallback=1'

# Create your views here.
#ana sayfa
#rewuest ana sayfaya istek

def home_view(request):
    results = None

    query = request.GET.get('query')
    if query:
        log, created = Search.objects.get_or_create(tag=query)
        log.save()
        url = API.format(API_KEY, query)
        results = requests.get(url).json()

    recent_searches = Search.objects.order_by('-search_date')[0:20]

    if len(recent_searches) == 0:
        recent_searches = None

    content = {
        'results': results,
        'recent_searches': recent_searches,

    }
    return render(request, 'home.html',content)
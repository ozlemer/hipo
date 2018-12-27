from django.shortcuts import render
from home.models import Search
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


API_KEY = '1ddb7df62cbdc4e07f6ec75ca78e2960'
API = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&tags={}&format=json&nojsoncallback=1'

# Create your views here.

def home_view(request):
    pictures = None
    #picture_list = None
    query = request.GET.get('query')
    if query:
        log, created = Search.objects.get_or_create(tag=query)
        log.save()
        url = API.format(API_KEY, query)
        picture_list = requests.get(url).json()
        paginator = Paginator(picture_list['photos']['photo'], 4)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            pictures = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            pictures = paginator.page(1)
        except EmptyPage:
            pictures = paginator.page(paginator.num_pages)
    # If page is out of range (e.g. 9999), deliver last page of results.

    recent_searches = Search.objects.order_by('-search_date')[0:20]

    if len(recent_searches) == 0:
        recent_searches = None
    content = {
        'pictures': pictures,
        'recent_searches': recent_searches,

    }
    return render(request, 'home.html',content)
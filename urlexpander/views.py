from django.shortcuts import render, get_object_or_404
import requests
from bs4 import BeautifulSoup
from .models import URL

def url_home(request):
	urls = URL.objects.all()
	return render(request, 'urlexpander/url_home.html', {'urls' : urls})

def url_detail(request, url_pk):
	url = get_object_or_404(URL, pk=pk)
	return render(request, 'urlexpander/url_detail.html', {'url' : url})

def url_add(request):
	origin = request.POST['origin']
	newUrl = URL()
	page = requests.get(origin)
	if html.status_code == 200:
		beatSoup = BeautifulSoup(page.content)
		newUrl.title = beatSoup.page.head.title.contents[0]
	else:
		newUrl.title = "Not availible"
	newUrl.origin = origin
	newUrl.dest = page.url
	newUrl.status = page.status_code
	newUrl.save()
	return render(request, 'urlexpander/url_detail.html', {'url' : newUrl})

def url_delete(request, url_pk):
	url = get_object_or_404(URL, pk=pk)
	url.delete()
	return render(request, 'urlexpander/url_home.html', {'urls' : URL.objects.all()})

from django.http import HttpResponse
from script.main import save_url
def save_page(request):
    url = request.GET.get('url')
    return HttpResponse(save_url(url))
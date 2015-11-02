from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def download(request):
    if request.method == 'POST':
        form = request.POST
        url = form.get('git_url')
        if url and url.startswith(("http", "ssh", "git")):
            return render(request, 'download.html', {'git_url': url})
        else:
            context = {'error_message': 'bad url'}
            return render(request, 'index.html', context)

    else:
        return HttpResponse("your are dummy")

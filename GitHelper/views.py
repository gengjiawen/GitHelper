import os
import subprocess

import shutil
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def download(request):
    if request.method == 'POST':
        form = request.POST
        url = form.get('git_url')
        if url and url.startswith(("http", "ssh", "git")):
            project = url[url.rfind("/") + 1:]
            location = r"/tmp/{}".format(project)
            if os.path.exists(location):
                shutil.rmtree(location)
            p = subprocess.Popen(['git', 'clone', url, location])
            p.communicate()
            archive_name = '/tmp/{}.7z'.format(project)
            if os.path.exists(archive_name):
                os.remove(archive_name)
            p = subprocess.Popen(['7z', 'a', archive_name, location],)
            p.communicate()
            print("done")
            return render(request, 'download.html', {'git_url': url})
        else:
            context = {'error_message': 'bad url'}
            return render(request, 'index.html', context)

    else:
        return HttpResponse("your are dummy")

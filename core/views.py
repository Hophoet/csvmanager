from django.shortcuts import render, HttpResponse, Http404, reverse
from django.conf import settings

import os
import os.path
import pandas
from .forms import CsvModalForm
from .models import Csv


def index(request):
    context = {}
    form = CsvModalForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            file1 = data['file1']
            file2 = data['file2']
            csv_manager(file1, file2)
            PROJECT_ROOT = os.path.abspath(os.path.dirname('csvs/'))
            print(PROJECT_ROOT)
            # print(data)
            # r = pandas.read_csv(file1)
            # print(r)
            # print(dir(file))
            file = PROJECT_ROOT+'/update.csv'
            context['file'] = file
            return download(request, file)

    context['form'] = form
    return render(request, 'core/index.html', context)


def csv_manager(file1, file2):
    fileone = file1.readlines()
    filetwo = file2.readlines()

    with open('csvs/update.csv', 'w') as outFile:
        for line in filetwo:
            if line not in fileone:
                line = line.decode()
                # print(type(line.decode('ascii')))
                outFile.write(line)

        for line in fileone:
            if line not in filetwo:
                line = line.decode()
                # print(type(line.decode('ascii')))
                outFile.write(line)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404

from django.shortcuts import render, HttpResponse, Http404, reverse
from django.conf import settings
from django.contrib import messages

import os
import os.path
import pandas
from .forms import CsvModalForm
from .models import Csv
from .csv import CSV


def index(request):
    context = {}
    form = CsvModalForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            file1 = data['file1']
            file2 = data['file2']
            action = data['actions']
            CSV.get_difference(file1, file2)
            PROJECT_ROOT = os.path.abspath(os.path.dirname('csvs/'))
            file = PROJECT_ROOT+'/update.csv'
            context['file'] = file
            return download(request, file)
            # if CSV.files_are_same_columns(file1, file2):
            #     if action == 'DIF':
            #         CSV.get_difference(file1, file2)
            #         PROJECT_ROOT = os.path.abspath(os.path.dirname('csvs/'))
            #         file = PROJECT_ROOT+'/update.csv'
            #         context['file'] = file
            #         return download(request, file)
            messages.info(request, 'actions not available')

            # else:
            #     messages.info(request, 'files are not compatible')

    context['form'] = form
    return render(request, 'core/index.html', context)


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

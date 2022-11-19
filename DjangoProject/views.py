from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def project_index(request):

    return render(request, 'index/index.html', {})

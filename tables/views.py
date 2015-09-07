from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from tables.models import Table

def table_home(request):
    # get all the posts
    table_list = Table.objects.all()
    return render(
                request,
                'table.html',
                {'table_list': table_list}
            )

def table_detail(request, id):
    table = Table.objects.get(id=id)
    return render(
                request, 
                'table_detail.html', 
                {'table': table}
            )

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from trips.models import Trip

def trip_home(request):
    # get all the posts
    trip_list = Trip.objects.all()
    return render(
                request,
                'trip.html',
                {'trip_list': trip_list}
            )

def trip_detail(request, id):
    trip = Trip.objects.get(id=id)
    return render(
                request, 
                'trip_detail.html', 
                {'trip': trip}
            )

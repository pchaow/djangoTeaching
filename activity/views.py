from django.http import HttpResponse
from django.shortcuts import render

from .forms import ActivityForm
from .models import Activity

# Create your views here.
def index(request):

    if request.POST :
        newAct = Activity()
        newAct.activity_name = request.POST['activity_name']
        newAct.activity_type = request.POST['activity_type']
        newAct.activity_desc = request.POST['activity_desc']
        newAct.save()

    activities = Activity.objects.all()
    activityForm = ActivityForm()

    return render(request,"activity/index.html",{
        'title' : "Hello From Title",
        'activities' : activities,
        "activityForm" : activityForm
    })
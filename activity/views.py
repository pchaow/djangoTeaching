from django.http import HttpResponse
from django.shortcuts import render

from .forms import ActivityForm
from .models import Activity


# Create your views here.
def index(request):
    editActivity = None
    if 'editId' in request.GET:
        editActivity = Activity.objects.get(id=request.GET['editId'])

    if request.POST:
        createForm = ActivityForm(request.POST,instance=editActivity)
        if (createForm.is_valid()):
            newAct = createForm.save(commit=False)
            newAct.save()
        editActivity = None

    activities = Activity.objects.all()
    if editActivity :
        activityForm = ActivityForm(instance=editActivity)
    else :
        activityForm = ActivityForm()

    return render(request, "activity/index.html", {
        'title': "Hello From Title",
        'activities': activities,
        "activityForm": activityForm,
        'editActivity' : editActivity
    })

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.template import Context, Template

from models import AthResults
from forms import QueryForm
import json

# Create your views here.
def index(request):
    indexContext = {}

    if request.GET and request.method == 'GET':
        school_choice = request.GET.get('school_choice')
        sex_choice = request.GET.get('sex_choice')
        event_choice = request.GET.get('event_choice')
        name_choice = request.GET.get('name_choice')
        
        # Get results
        results = AthResults.objects.filter(event=event_choice, name=name_choice)
        indexContext['results'] = results

        # Prepare form again
        form = QueryForm(initial={'school_choice': school_choice,
                                  'sex_choice': sex_choice,
                                  'event_choice': event_choice,
                                  'name_choice': name_choice,
                                  })        
    else:
        form = QueryForm(initial={'school_choice': None})
        
    indexContext['form'] = form
    return render(request, 'ath_res_vis/index.html', indexContext)

def get_school_info(request):
    school_choice = request.GET.get('school_choice', None)
    sex_choice = request.GET.get('sex_choice', None)
    event_choice = request.GET.get('event_choice', None)
    
    if school_choice: # Valid school name
        school_athlete_list = AthResults.objects.filter(school=school_choice).order_by('name')
    else:
        school_athlete_list = AthResults.objects.none()

    sex_list = school_athlete_list.order_by('-sex').values_list('sex', flat=True).distinct()    
    event_list = school_athlete_list.order_by('event').values_list('event', flat=True).distinct()

    # Get back name list
    if len(sex_list) > 0 and not sex_choice:
        sex_choice = sex_list[0]

    if len(event_list) > 0 and not event_choice:
        event_choice = event_list[0]

    if sex_choice and event_choice:
        athlete_list = AthResults.objects.filter(school=school_choice, event=event_choice, sex=sex_choice).order_by('name')
    else:
        athlete_list = AthResults.objects.none()

    sex_list = set(sex_list)
    name_list = athlete_list.values_list('name', flat=True).distinct()

    # Convert all lists to ASCII
    sex_list = [sex.encode('ascii') for sex in sex_list]
    event_list = [event.encode('ascii') for event in event_list]
    name_list = [name.encode('ascii') for name in name_list]

    data = {
        'sex_list': json.dumps(sex_list),
        'event_list': json.dumps(event_list),
        'name_list': json.dumps(name_list),
    }
    
    return JsonResponse(data)

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.template import Context, Template

from models import AthResults
from forms import QueryForm, get_list
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
        results = AthResults.objects.filter(
            school=school_choice,
            sex=sex_choice,
            event=event_choice, 
            name=name_choice)
        indexContext['results'] = results

        # Prepare data
        if len(results) > 0:
            is_track = results[0].is_track
        else:
            is_track = 0
        plot_x = [res.date.strftime('%Y-%m-%d') for res in results]
        plot_y = [res.result for res in results]

        # Prepare form
        form = QueryForm(initial={'school_choice': school_choice,
                                  'sex_choice': sex_choice,
                                  'event_choice': event_choice,
                                  'name_choice': name_choice,
                                  })        
    else:
        # Prepare data
        is_track = 0
        plot_x = []
        plot_y = []

        # Prepare form
        form = QueryForm(initial={'school_choice': None,
                                  'sex_choice': None,
                                  'event_choice': None,
                                  'name_choice': None,
                                  })
        
    indexContext['is_track'] = is_track
    indexContext['plot_x'] =  json.dumps(plot_x)
    indexContext['plot_y'] =  json.dumps(plot_y)
    indexContext['form'] = form

    return render(request, 'ath_res_vis/index.html', indexContext)

def get_info(request):
    school_choice = request.GET.get('school_choice', None)
    sex_choice = request.GET.get('sex_choice', None)
    event_choice = request.GET.get('event_choice', None)
    
    sex_list, event_list, name_list = get_list(school_choice, sex_choice, event_choice)

    # Convert all lists to ASCII
    sex_list = set(sex_list)
    sex_list = [sex.encode('ascii') for sex in sex_list]
    event_list = [event.encode('ascii') for event in event_list]
    name_list = [name.encode('ascii') for name in name_list]

    data = {
        'sex_list': json.dumps(sex_list),
        'event_list': json.dumps(event_list),
        'name_list': json.dumps(name_list),
    }
    
    return JsonResponse(data)

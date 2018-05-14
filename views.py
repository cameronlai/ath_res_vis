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

    # TODO: Review whether this kind of sorting method is the best thing to do
    form = QueryForm()
    indexContext['form'] = form

    """
    if request.POST and request.method == 'POST':
        print('In Post Method')

        selected_school = request.POST.get('school_choice')
        form.set_selected_school(selected_school)

        selected_name = request.POST.get('name_choice')
        name_list = AthResults.objects.filter(school=selected_school).order_by('name')
        name_list = name_list.values_list('name', flat=True).distinct()
        form.set_name_choice(name_list, selected_name)

        selected_event = request.POST.get('event_choice')ma manage.py shell
      event_list = AthResults.objects.filter(name=selected_name).order_by('event')
        event_list = event_list.values_list('event', flat=True).distinct()
        form.set_event_choice(event_list, selected_event)

        if selected_name != None and selected_event != None:
            print(selected_name)
            print(selected_event)
            results = AthResults.objects.filter(name=selected_name, 
                                                event=selected_event)
    else:
        print('do nothing')
    """
    indexContext['form'] = form
    """
    indexContext['school_form'] = school_form
    indexContext['school_list'] =  school_list
    indexContext['results'] = results
    """      
    return render(request, 'ath_res_vis/index.html', indexContext)

def get_school_info(request):
    schoolname = request.GET.get('schoolname', None)
    print(schoolname)
    athlete_list = AthResults.objects.filter(school=schoolname).order_by('name')

    if len(athlete_list) > 0:
        name_list = athlete_list.values_list('name', flat=True).distinct()
        sex_list = athlete_list.values_list('sex', flat=True).distinct()
        sex_list = set(sex_list)
    else:
        sex_list = AthResults.objects.all().values_list('sex', flat=True).distinct()
        
    name_list = [name.encode('ascii') for name in name_list]
    sex_list = [sex.encode('ascii') for sex in sex_list]

    data = {
        'name_list': json.dumps(name_list),
        'sex_list': json.dumps(sex_list),
    }
    
    return JsonResponse(data)

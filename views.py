from django.shortcuts import render, HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.template import Context, Template

from models import AthResults
from forms import QueryForm, SchoolForm

# Create your views here.
def index(request):
    indexContext = {}

    # TODO: Review whether this kind of sorting method is the best thing to do
    school_list = AthResults.objects.order_by('school').values_list('school', flat=True).distinct()
    form = QueryForm(school_list, None)
    school_form = SchoolForm(school_list)
    results = None

    if request.POST and request.method == 'POST':
        print('In Post Method')

        selected_school = request.POST.get('school_choice')
        form.set_selected_school(selected_school)

        selected_name = request.POST.get('name_choice')
        name_list = AthResults.objects.filter(school=selected_school).order_by('name')
        name_list = name_list.values_list('name', flat=True).distinct()
        form.set_name_choice(name_list, selected_name)

        selected_event = request.POST.get('event_choice')
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

    indexContext['form'] = form
    indexContext['school_form'] = school_form
    indexContext['school_list'] =  school_list
    indexContext['results'] = results
        
    return render(request, 'ath_res_vis/base.html', indexContext)

def load_names(request):
    print('load_names function')
    print(request)
    school = request.GET.get('school')
    name_list = AthResults.objects.filter(school=school).order_by('name')
    indexContext = {'name_list': name_list}
    return render(request, 'ath_res_vis/name_dropdown_list.html', indexContext)

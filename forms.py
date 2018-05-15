from django import forms
from models import AthResults

def get_list(school_choice, sex_choice, event_choice):
    if school_choice: # Valid school name%se
        school_athlete_list = AthResults.objects.filter(school=school_choice).order_by('name')
    else:
        school_athlete_list = AthResults.objects.none()
        
    sex_list = school_athlete_list.order_by('-sex').values_list('sex', flat=True).distinct()    
    event_list = school_athlete_list.order_by('event').values_list('event', flat=True).distinct()

    # Get back name list
    if len(sex_list) > 0 and not sex_choice in sex_list:
        sex_choice = sex_list[0]

    if len(event_list) > 0 and not event_choice in event_list:
        event_choice = event_list[0]

    if sex_choice and event_choice:
        athlete_list = AthResults.objects.filter(school=school_choice, event=event_choice, sex=sex_choice).order_by('name')
    else:
        athlete_list = AthResults.objects.none()

    name_list = athlete_list.values_list('name', flat=True).distinct()

    return sex_list, event_list, name_list

class QueryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)

        # Get back list 
        school_list = AthResults.objects.order_by('school').values_list('school', flat=True).distinct()

        school_choice = self.initial['school_choice']
        sex_choice = self.initial['sex_choice']
        event_choice = self.initial['event_choice']
        sex_list, event_list, name_list = get_list(school_choice, sex_choice, event_choice)

        # Update form fields
        self.fields['school_choice'] = forms.ModelChoiceField(
            queryset=school_list,
            label='School',
            )
        self.fields['sex_choice'] = forms.ModelChoiceField(
            queryset=sex_list,
            label='Sex',
            empty_label=None,
            )
        self.fields['event_choice'] = forms.ModelChoiceField(
            queryset=event_list,
            label='Event',
            empty_label=None,
            )
        self.fields['name_choice'] = forms.ModelChoiceField(
            queryset=name_list,
            label='Name',
            empty_label=None,
            )

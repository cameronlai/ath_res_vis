from django import forms
from models import AthResults

class QueryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)

        # Get back choices
        school_choice = AthResults.objects.order_by('school').values_list('school', flat=True).distinct()
        sex_choice = AthResults.objects.values_list('sex', flat=True).distinct()
        event_choice = AthResults.objects.order_by('event').values_list('event', flat=True).distinct()
    
        # Update form fields
        self.fields['school_choice'] = forms.ModelChoiceField(queryset=school_choice)
        self.fields['sex_choice'] = forms.ModelChoiceField(queryset=sex_choice)
        self.fields['name_choice'] = forms.ModelChoiceField(queryset=AthResults.objects.none())
        self.fields['event_choice'] = forms.ModelChoiceField(queryset=event_choice)    

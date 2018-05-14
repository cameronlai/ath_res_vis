from django import forms
from models import AthResults

class QueryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)

        # Get back list for 
        school_list = AthResults.objects.order_by('school').values_list('school', flat=True).distinct()
        sex_list = AthResults.objects.none()
        event_list = AthResults.objects.none()
        name_list = AthResults.objects.none()
    
        # Update form fields
        self.fields['school_choice'] = forms.ModelChoiceField(queryset=school_list)
        self.fields['sex_choice'] = forms.ModelChoiceField(queryset=sex_list)
        self.fields['event_choice'] = forms.ModelChoiceField(queryset=event_list)
        self.fields['name_choice'] = forms.ModelChoiceField(queryset=name_list)

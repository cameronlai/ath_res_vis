from django import forms
from models import AthResults

class QueryForm(forms.Form):
    def __init__(self, school_list, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['school_choice'] = forms.ModelChoiceField(queryset=school_list)
        self.fields['name_choice'] = forms.ModelChoiceField(queryset=school_list)
        self.fields['event_choice'] = forms.ModelChoiceField(queryset=school_list)

    def set_name_choice(self, name_list, selected_name):
        self.fields['name_choice'] = forms.ModelChoiceField(queryset=name_list)
        self.initial['name_choice'] = selected_name

    def set_event_choice(self, event_list, selected_event):
        self.fields['event_choice'] = forms.ModelChoiceField(queryset=event_list)
        self.initial['event_choice'] = selected_event

    def set_selected_school(self, selected_school):
        self.initial['school_choice'] = selected_school

class SchoolForm(forms.Form):
    def __init__(self, school_list, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.fields['school_choice'] = forms.ModelChoiceField(queryset=school_list)

    

from django import forms
from .models import LaunchedGovProjects




class LaunchedGovProjectForm(forms.ModelForm):
    class Meta:
        model = LaunchedGovProjects
        fields = [
            'project_title', 'status', 'location', 'launched_by',
            'contractor', 'amount_allocated', 'overview','project_start_date','project_end_date',
            'reporter_name', 'reporter_phone_number'
        ]
        widgets = {
            'overview': forms.Textarea(attrs={'rows': 4}),
            
        }

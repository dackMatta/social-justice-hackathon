# forms.py
from django import forms
from .models import Case,Authority,Comment

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['case_type', 'description', 'anonymous_name', 'anonymous_email', 'attachment', 'phone_number', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class CaseAssignmentForm(forms.Form):
    lawyer = forms.ModelChoiceField(queryset=Authority.objects.all(), empty_label="Select a lawyer")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['sender','subject','content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Type your message here...',
                'class': 'form-control'
            }),
        }
        labels = {
            'content': '', 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = True
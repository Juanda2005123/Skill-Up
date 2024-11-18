from django import forms
from django.forms import ModelForm
from .models import Project, Deliverable, Milestone
from django.core.exceptions import ValidationError

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['client', 'version']

    def clean_Budget(self):
        budget = self.cleaned_data.get('budget')
        if budget <= 0:
            raise ValidationError('Budget must be a positive value.')
        return budget

    def clean_daysDuration(self):
        days_duration = self.cleaned_data.get('daysDuration')
        if days_duration <= 0:
            raise ValidationError('Days duration must be a positive integer.')
        return days_duration

class DeliverableForm(forms.ModelForm):
    class Meta:
        model = Deliverable
        fields = ['name', 'description', 'deadlineInDays', 'requiresEvidence']


class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['name']
        
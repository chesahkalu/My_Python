from django import forms
from .models import Baby, Milestone

class MilestoneLogForm(forms.ModelForm):
    logged_milestones = forms.ModelMultipleChoiceField(
        queryset=Milestone.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False  # Remove the 'required' attribute
    )

    class Meta:
        model = Baby
        fields = ['logged_milestones']

    def __init__(self, *args, **kwargs):
        baby = kwargs.pop('baby', None)
        grouped_milestones = kwargs.pop('grouped_milestones', None)
        super().__init__(*args, **kwargs)
        if baby:
            self.fields['logged_milestones'].queryset = Milestone.objects.filter(month=baby.age_in_months)
        if grouped_milestones:
            self.grouped_milestones = grouped_milestones

    def get_initial_for_field(self, field, field_name):
        if field_name == 'logged_milestones':
            initial = self.initial.get(field_name, [])
            return initial
        return super().get_initial_for_field(field, field_name)

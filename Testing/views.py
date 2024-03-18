from django.shortcuts import render, redirect
from .forms import MilestoneLogForm
from .models import Milestone, Activity, NutritionGuide
from babies.models import Baby

from django.shortcuts import render, redirect
from .forms import MilestoneLogForm
from .models import Milestone, Activity, NutritionGuide
from babies.models import Baby
from itertools import groupby


def log_milestone(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    milestones = Milestone.objects.filter(month=baby.age_in_months)

    grouped_milestones = {}
    for milestone in milestones:
        grouped_milestones.setdefault(milestone.area, []).append((milestone.id, milestone.description))

    if request.method == 'POST':
        form = MilestoneLogForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            return redirect('babies:baby_detail', baby_id=baby.id)
    else:
        initial_milestones = baby.logged_milestones.values_list('id', flat=True)  # Get the initially logged milestones
        form = MilestoneLogForm(instance=baby, baby=baby, grouped_milestones=grouped_milestones, initial={'logged_milestones': initial_milestones})

    return render(request, 'milestones/log_milestone.html', {'form': form})






def view_expected_milestones(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    expected_milestones = Milestone.objects.filter(month=baby.age_in_months)
    return render(request, 'milestones/view_expected_milestones.html', {'expected_milestones': expected_milestones, 'baby': baby})

def view_activities(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    activities = Activity.objects.filter(month=baby.age_in_months)
    return render(request, 'milestones/activities.html', {'activities': activities, 'baby': baby})

def view_nutrition_guide(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    nutrition_guide = NutritionGuide.objects.filter(month=baby.age_in_months)
    return render(request, 'milestones/nutrition_guide.html', {'nutrition_guide': nutrition_guide, 'baby': baby})

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Branches


def branches(request):
    all_branches = Branches.objects.all()
    return render(request, 'branches/branchesAbout.html', {'branches':all_branches})


class BranchDetailView(DetailView):
    model = Branches
    template_name = 'branches/branch_template.html'
    context_object_name = "branch"

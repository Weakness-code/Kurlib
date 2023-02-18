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

    def get_object(self, queryset=None):
        obj = super(BranchDetailView, self).get_object(queryset=queryset)
        obj.edited_description = info_editor(obj.description)
        obj.images = []
        for i in range(20):
            try:
                eval(f"obj.images.append(obj.image_{i}.url)")
            except ValueError:
                break
        return obj

def info_editor(info: str):
    text = info.split("\n")
    return text
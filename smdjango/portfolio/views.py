from django.shortcuts import render
from .models import Category
from .models import Projects
from django.views.generic import DeleteView

def portfolio_index(request):
    categories = Category.objects.all()
    projects = Projects.objects.prefetch_related("project_images").all().order_by('сreated').reverse()
    return render(request, 'portfolio/portfolio_index.html', {'categories': categories, 'projects': projects})

class ProjectsDeleteView(DeleteView):
    model = Projects
    template_name = 'portfolio/details_view.html'
    context_object_name = 'project'
from django.shortcuts import render, redirect
from .forms import AssignmentForm
from .models import Assignment

def home(request):
    return render(request, 'assignment/home.html')


def submit_assignment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        request.session['student_name'] = name

        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student_name = name
            assignment.save()
            return redirect('list')
    else:
        form = AssignmentForm()

    return render(request, 'assignment/submit.html', {'form': form})


def list_assignments(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignment/list.html', {'assignments': assignments})

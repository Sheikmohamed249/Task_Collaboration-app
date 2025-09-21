from django.contrib.auth.forms import UserCreationForm

# Signup view
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})

import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm
from django.utils import timezone

@login_required
def export_tasks_csv(request):
	user = request.user
	tasks = Task.objects.filter(created_by=user) | Task.objects.filter(assigned_to=user)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="tasks.csv"'
	writer = csv.writer(response)
	writer.writerow(['Title', 'Description', 'Deadline', 'Priority', 'Assigned To', 'Created By', 'Status'])
	for task in tasks.distinct():
		writer.writerow([
			task.title,
			task.description,
			task.deadline,
			task.priority,
			task.assigned_to.username,
			task.created_by.username,
			task.status
		])
	return response

@login_required
def dashboard(request):
	user = request.user
	# Filtering and sorting
	status_filter = request.GET.get('status')
	sort_by = request.GET.get('sort')
	created_tasks = Task.objects.filter(created_by=user)
	assigned_tasks = Task.objects.filter(assigned_to=user)
	if status_filter:
		created_tasks = created_tasks.filter(status=status_filter)
		assigned_tasks = assigned_tasks.filter(status=status_filter)
	if sort_by:
		created_tasks = created_tasks.order_by(sort_by)
		assigned_tasks = assigned_tasks.order_by(sort_by)
	# Analytics
	completed_count = Task.objects.filter(created_by=user, status='Completed').count()
	pending_count = Task.objects.filter(created_by=user, status='Pending').count()
	assigned_completed = Task.objects.filter(assigned_to=user, status='Completed').count()
	assigned_pending = Task.objects.filter(assigned_to=user, status='Pending').count()
	return render(request, 'tasks/dashboard.html', {
		'created_tasks': created_tasks,
		'assigned_tasks': assigned_tasks,
		'now': timezone.now(),
		'status_filter': status_filter,
		'sort_by': sort_by,
		'completed_count': completed_count,
		'pending_count': pending_count,
		'assigned_completed': assigned_completed,
		'assigned_pending': assigned_pending,
	})

@login_required
def create_task(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.created_by = request.user
			task.save()
			return redirect('dashboard')
	else:
		form = TaskForm()
	return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def update_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
	else:
		form = TaskForm(instance=task)
	return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

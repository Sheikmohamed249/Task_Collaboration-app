
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	PRIORITY_CHOICES = [
		('Low', 'Low'),
		('Medium', 'Medium'),
		('High', 'High'),
	]
	STATUS_CHOICES = [
		('Pending', 'Pending'),
		('Completed', 'Completed'),
	]
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	deadline = models.DateTimeField()
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
	assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

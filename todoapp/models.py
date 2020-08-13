from django.db import models


class TaskInfo(models.Model):
	title = models.CharField(max_length = 20)
	content = models.CharField(max_length = 100)
	
	class Meta:
		ordering = ['-id']

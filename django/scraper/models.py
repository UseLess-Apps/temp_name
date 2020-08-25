from django.db import models

MAX_LENGTH = 300

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=MAX_LENGTH)
    description = models.CharField(blank=True, max_length=MAX_LENGTH)
    company = models.CharField(max_length=MAX_LENGTH)
    posted_date = models.DateField()
    work_type = models.CharField(max_length=MAX_LENGTH)
    location = models.CharField(blank=True, max_length=MAX_LENGTH)

    def __str__(self):
        return f'id: {self.id}, title: {self.title}'

class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

class Job_to_Tag(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'id: {self.id}, job_id: {self.job_id}, tag_id: {self.tag_id}'
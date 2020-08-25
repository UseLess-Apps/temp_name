from django.contrib import admin
from .models import Job, Tag, Job_to_Tag

# Register your models here.

admin.site.register(Job)
admin.site.register(Tag)
admin.site.register(Job_to_Tag)

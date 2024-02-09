from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/images/')
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    date_created = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

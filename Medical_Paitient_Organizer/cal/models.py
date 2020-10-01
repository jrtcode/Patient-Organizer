from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    @property
    def get_html_url_delete(self):
        url2 = reverse('cal:event_delete', args=(self.id,))
        return f"<a class='right2' href='{url2}'>x</a>"

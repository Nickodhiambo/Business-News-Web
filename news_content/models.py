from django.db import models

# Create your models here.


class Content(models.Model):
    """Defines business content data schema"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    pub_date = models.DateTimeField()
    guid = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100)
    site_logo = models.URLField(null=True)

    def __str__(self) -> str:
        """Returns a string representation of model"""
        return f"{self.site_name}: {self.title}"

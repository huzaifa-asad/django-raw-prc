from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pname = models.CharField("Page Name", max_length=255)
    pcat = models.CharField("Page Category", max_length=255)
    ppublished = models.DateField("Page Published Date")
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Post Title", max_length=255)
    ptcat = models.CharField("Post Category", max_length=255)
    ptpublished = models.DateField("Post Published Date", )
    
class Song(models.Model):
    user = models.ManyToManyField(User)
    sname = models.CharField("Song Name", max_length=255)
    sduration = models.IntegerField("Song Duration")
    
    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])

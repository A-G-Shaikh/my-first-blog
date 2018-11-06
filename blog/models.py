from django.db import models
from django.utils import timezone

# Create your models here. Models are saved in the SQLite database for this app.


class Post(models.Model):
    """The main post that the user will be making"""
    
    
    author =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    #Only allow moderated comments to appear.
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    """To allow visitors to make comments on posts"""
    
    #Link comments to their respective post.
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    #Allow people to add their name to their comment.
    author= models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #Moderate comments.
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.text


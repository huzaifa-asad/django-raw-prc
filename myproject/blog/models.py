from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrolled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.age})"
    
# Relationships in Models

## One-to-Many
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
# One-to-One
class PostDetail(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="detail")
    word_count = models.IntegerField()
    reading_time = models.IntegerField() # in minutes
    
    def __str__(self):
        return f"Details of {self.post.title}"
    
# Many-to-Many
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(Post, related_name="tags")
    
    def __str__(self):
        return self.name
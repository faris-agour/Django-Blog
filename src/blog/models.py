from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


def img_upload(instance, filename):
    imgname, ext = filename.split('.')
    return f'images/{instance.id}.{ext}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')  # one author has many posts
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('DR', 'Draft'),
        ('CR', 'Created'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='DF')
    image = models.ImageField(upload_to=img_upload)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

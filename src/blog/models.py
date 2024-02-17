from django.contrib.auth.models import User
from django.db import models

# Create your models here.
Status = (
    ("DF", "Draft"),
    ("CR", "Created"),
)


def img_upload(instance, filename):
    imgname, ext = filename.split('.')
    return f'jobs/{instance.id}.{ext}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')  # one author has many posts
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status)
    image = models.ImageField(upload_to=img_upload, blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

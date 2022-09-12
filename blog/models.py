from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    

class Post(models.Model):
    # d databasede görülme şekli diğeri kullanıcı menüdeki görünümü
    OPTIONS = (
        ("d", "Draft"),
        ("p","Published")
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    publisy_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default="d")
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
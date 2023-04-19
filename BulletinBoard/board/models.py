from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.author_user)


class News(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return '{}'.format(self.name)


class CategoryClass(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return '{}'.format(self.name)


class Advertisement(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    post_category = models.ManyToManyField(Category, through='AdvtCategory')
    class_category = models.ManyToManyField(CategoryClass, through='ClassCategory')
    upload = models.FileField(upload_to='uploads/')

    def preview(self):
        return '{}...'.format(self.text[0:19])

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('advt_detail', kwargs={'pk': self.pk})


class AdvtCategory(models.Model):
    post_through = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class ClassCategory(models.Model):
    post_through = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    category_through = models.ForeignKey(CategoryClass, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

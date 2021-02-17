from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.

class Golmok(models.Model):
    name = models.CharField(max_length=25, unique=True)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    head_image1 = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    head_image2 = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=25, unique=True)
    address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    # description = models.CharField(max_length=500, null=True)
    # rating = models.CharField(max_length=10)
    golmok = models.ForeignKey(Golmok, blank=True, null=True, on_delete=models.SET_NULL)
    # images = models.CharField(max_length=50, null=True)

    description = MarkdownxField(null=True)
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # 포스트가 생성이 될 때 created에 자동으로 담아주게 된다.
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/mukja/golmok/{}/{}/'.format(self.golmok.pk, self.pk)

    def get_markdown_description(self):
        return markdown(self.description)

class Menu(models.Model):
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=300, null=True)
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.SET_NULL)
    text = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    # 새로 생성됐을 때 저절로 시간이 들어가게끔
    modified_at = models.DateTimeField(auto_now=True)

    def get_markdown_content(self):
        return markdown(self.text)

    def get_absolute_url(self):
        return self.restaurant.get_absolute_url() + '#comment-id-{}'.format(self.pk)  # 해당 댓글로 바로 이동하기 위함.
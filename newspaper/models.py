from django.db import models
from django.contrib.auth.models import User 

class TimeStampModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #dont create table in DB


class Category(TimeStampModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"] #categoru.objects.all()
        verbose_name = "category"
        verbose_name_plural = "Categories"


class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return a string representation of the Tag, which is its name.
        """
        return self.name
   
 
# null = True => when there is no data in published_at, null value will be saved in db
# blank = True => no need to validate if the data is not provided


class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "Inactive"), #publish gareko post delete nagari user le herna namilen gari rakhne. hide gareko jastai
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    views_count = models.PositiveIntegerField(default=0)
    is_breaking_news = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
    

class Advertisement(TimeStampModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="advertisement/%Y/%m/%d", blank=False)

    def __str__(self):
        return self.title
    
class OurTeam(TimeStampModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team_image/%Y/%m/%d", blank=False)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Contact(TimeStampModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["created_at"]


class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.content[:50]} | {self.user.username}'
    
    
class Newsletter(TimeStampModel):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
    


# user - comment
# 1 user can add M comment => M
# 1 comment is associated to only 1 user => 1
# ForeignKey => M => comment

# comment - post
# 1 post can have M comments => M
# 1 comment is associated to only 1 post => 1
# ForeignKey => M => Comment





















# from django.db import models

# # Create your models here.
# #Post
# #title => Charfield
# #author => Relationship
# #published date => datetimefiled
# #view count => integer
# #category => Relationship
# #tags => Relationship
# #image => ImageField
# #content => TextField

# class TimeStampMode(models.Model):
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         abstract = True #Don't create table in DB
        
# class Category(TimeStampMode):
#     name = models.CharField(max_length=180)
#     icon = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         ordering = ["name"]
#         verbose_name = "category"
#         verbose_name_plural = "Categories"

# class Tag(TimeStampMode):
#     name= models.CharField(max_length=100)
    
#     def __str__(self):
#         """
#         Return a string representation of the Tag, which is its name.
#         """
#         return self.name
    
# #null = true => when there is no data in published_at null value will be saved in db
# #blank = True => no need to validate if the data is not provided

# class Post(TimeStampMode):
#     STATUS_CHOICES = [
#         ("active","Active"),
#         ("in_active", "Inactive"),
#     ]
    
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
#     author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
#     views_count = models.PositiveBigIntegerField(default=0)
#     is_breaking_news = models.BooleanField(default=False)
#     published_at = models.DateTimeField(null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE) 
#     tag = models.ManyToManyField(Tag)
    
#     def __str__(self):
#         return self.title 
    
# class Advertisement(TimeStampMode):
#     title = models.CharField(max_length=100)
#     image= models.ImageField(upload_to="advertisements/%Y/%m/%d", blank=False)
    
#     def __str__(self):
#         return self.title
    
from django.contrib import admin
from newspaper.models import Category, Post, Tag, Advertisement, OurTeam, Contact, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(OurTeam)
admin.site.register(Contact)
admin.site.register(Comment)



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
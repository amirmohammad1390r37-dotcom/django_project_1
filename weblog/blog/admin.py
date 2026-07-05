from django.contrib import admin
from.models import Post,User,Category,comment,Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(comment)
admin.site.register(Tag)
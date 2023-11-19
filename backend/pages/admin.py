from django.contrib import admin
from studio.models import Studio
from games.models import Game
from genre.models import Genre
from comments.models import Comment

admin.site.register(Comment)
admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Studio)
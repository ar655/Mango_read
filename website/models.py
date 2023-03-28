from django.db import models

from mango_read import settings








class Genre(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name



class Card(models.Model):
    name = models.CharField(max_length=45,default='name')
    type = models.CharField(max_length=45)
    year = models.IntegerField(default=2023)
    summary = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='cards', null=True)
    image = models.ImageField(null=True, upload_to='photos')

    def __str__(self):
        return self.name

    @property
    def genre_name(self):
        try:
            return self.genre.name
        except:
            return 'Not selected!'


class Comment(models.Model):
    post = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments',)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    class Meta:

        ordering = ('created',)

    def __str__(self):

        return f'Comment by {self.username} on {self.post}'



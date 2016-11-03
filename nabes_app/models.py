from django.db import models
from django.contrib.auth.models import User # creates user
from django.db.models.signals import post_save # enables profile attached to user
from django.dispatch import receiver # enables profile attached to user
from django.contrib.staticfiles.templatetags.staticfiles import static # default image for photo_urls


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    photo = models.ImageField(upload_to='profile_photos', verbose_name='Profile photo')
    email = models.EmailField(max_length=50)

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return static('nabes_app/img/w.png')


class PublicPost(models.Model):
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post_photos')
    author = models.ForeignKey('auth.User')

    class Meta:
        ordering = ['-created']


class MemberPost(models.Model):
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post_photos')
    author = models.ForeignKey('auth.User')

    class Meta:
        ordering = ['-created']


class BoardPost(models.Model):
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post_photos')
    author = models.ForeignKey('auth.User')

    class Meta:
        ordering = ['-created']


class Newsletter(models.Model):
    document = models.FileField(upload_to='documents') # have it verify a pdf?
    author = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def document_url(self):
        if self.document:
            return self.document.url
        return static('nabes_app/img/newsletter_default.pdf')


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        Profile.objects.create(user=instance)

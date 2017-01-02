from django.db import models
from django.contrib.auth.models import User # creates user
from django.db.models.signals import post_save # enables profile attached to user
from django.dispatch import receiver # enables profile attached to user
from django.contrib.staticfiles.templatetags.staticfiles import static # default image for photo_urls


class Profile(models.Model):
    resident = models.OneToOneField('auth.User')
    primary_last_name = models.CharField(max_length=50, default='')
    secondary_last_name = models.CharField(max_length=50, default='', null=True, blank=True)
    primary_phone = models.CharField(max_length=12, default='')
    secondary_phone = models.CharField(max_length=12, default='', null=True, blank=True)
    family_members = models.CharField(max_length=200, default='', null=True, blank=True)
    # photo = models.ImageField(upload_to='profile_photos', verbose_name='Profile photo')
    primary_email = models.EmailField(max_length=50, null=True, blank=True)
    house_number = models.PositiveIntegerField(null=True, blank=True)
    street = models.CharField(max_length=50, default='')
    membership_status = models.CharField(max_length=20, default='') #make this a choice list
    paypal = models.CharField(max_length=10, default='') #capture paypal
    check = models.CharField(max_length=10, default='') #manual input
    resident_status = models.CharField(max_length=5, default='') #make this a choice list to keep directory current

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return static('nabes_app/img/westport_1.jpg')

    def __str__(self):
        return self.primary_last_name


class PublicPost(models.Model):
    headline = models.CharField(max_length=60, default='')
    body = models.TextField(max_length=900)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post_photos')
    author = models.ForeignKey('auth.User')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.headline

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url


class MemberPost(models.Model):
    headline = models.CharField(max_length=60, default='')
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post_photos')
    author = models.ForeignKey('auth.User')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-created']


class BoardPost(models.Model):
    headline = models.CharField(max_length=60, default='')
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post_photos')
    author = models.ForeignKey('auth.User')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-created']


class Newsletter(models.Model):
    document = models.FileField(upload_to='documents', max_length=200) # max_length required!!!
    headline = models.CharField(max_length=50, default='Month: Highlight here')
    author = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    @property
    def document_url(self):
        if self.document:
            return self.document.url
        return static('nabes_app/img/newsletter_default.pdf')

class Officer(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    term = models.CharField(max_length=7)

    def __str__(self):
        return self.name

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        Profile.objects.create(resident=instance)

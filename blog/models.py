from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset()\
                        .filter(status='dimuat')


class Konten(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('dimuat', 'Dimuat'),
    )
    judul = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='terbit')
    penulis = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='blog_posts')
    body = models.TextField()
    kategori = models.CharField(max_length=20,
                                default='Kehidupan')
    terbit = models.DateTimeField(default=timezone.now)
    dibuat = models.DateTimeField(auto_now_add=True)
    diperbarui = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')

    class Meta:
        ordering = ('-terbit',)
        verbose_name_plural = 'Seluruh Konten'

    def __str__(self):
        return self.judul

    objects = models.Manager()   # The default manager.
    dimuat = PublishedManager()   # Our custom manager.

    def get_absolute_url(self):
        return reverse('blog:konten_detail',
                        args = [self.terbit.year,
                                self.terbit.month,
                                self.terbit.day,
                                self.slug])

class Komentar(models.Model):
    konten = models.ForeignKey(Konten, on_delete=models.CASCADE,
                                        related_name='seluruh_komentar')
    nama = models.CharField(max_length=80)
    email = models.EmailField()
    isi = models.TextField()
    dibuat = models.DateTimeField(auto_now_add=True)
    diperbarui = models.DateTimeField(auto_now=True)
    aktif = models.BooleanField(default=True)

    class Meta:
        ordering = ('dibuat',)
        verbose_name_plural = 'Seluruh Komentar'

    def __str__(self):
        return f'Komentar dari {self.nama} pada {self.konten}'

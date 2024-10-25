from django.db import models

class Video(models.Model):# Create your models here
  title = models.CharField(max_length=100, unique=True, verbose_name='Titulo')
  description = models.TextField(verbose_name='Descrição')
  thumbnail = models.ImageField(upload_to='thumbnail/', verbose_name='Thumbnail')
  slug = models.SlugField(unique=True)
  published_at = models.DateTimeField(verbose_name='Publicado em', null=True, editable=False)
  is_published = models.BooleanField(default=False, verbose_name='Publicado')
  num_likes = models.IntegerField(default=0, verbose_name='Likes', editable=False)
  num_views = models.IntegerField(default=0, verbose_name='Visualizações', editable=False)
  tags = models.ManyToManyField('Tag', verbose_name='Tags', related_name='videos')

  class Meta:
    verbose_name = 'Video'
    verbose_name_plural = 'Videos'

  def __str__(self):
    return self.title


class VideoMedia(models.Model):

  class Status(models.TextChoices):
        UPLOADED_STARTED = 'UPLOADED_STARTED', 'Upload Iniciado'
        PROCESS_STARTED = 'PROCESSING_STARTED', 'Processamento Iniciado'
        PROCESS_FINISHED = 'PROCESSING_FINISHED', 'Processamento Finalizado'
        PROCESS_ERROR = 'PROCESSING_ERROR', 'Erro no Processamento'

  video_path = models.CharField(max_length=255, verbose_name='Vídeo')
  status = models.CharField(max_length=20, choices=Status.choices, default=Status.UPLOADED_STARTED, verbose_name='Status')
  video = models.OneToOneField('Video', on_delete=models.PROTECT, verbose_name='Vídeo', related_name='video_media')

  class Media:
    verbose_name = 'Midia'
    verbose_name_plural = 'Midias'

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True, verbose_name='Nome')

  class Meta:
    verbose_name = 'Video'
    verbose_name_plural = 'Videos'

  def __str__(self):
    return self.title


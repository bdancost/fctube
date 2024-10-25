from django.db import models

# Create your models here
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
from django.db import models
# Заголовок статьи
# URL-адрес происхождения или источника
# URL изображения статьи

class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()

  def __str__(self):
    return self.title

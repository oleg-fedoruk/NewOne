from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    body = models.TextField(verbose_name='Публикация')
    image = models.ImageField(verbose_name='Картинка', upload_to='pictures', blank=True, null=True)
    file = models.FileField(verbose_name='Приложение', upload_to='files', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

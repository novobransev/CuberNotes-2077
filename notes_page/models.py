from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Notes(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Заголовок')
    descriptions = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    important = models.BooleanField(blank=True, verbose_name='Важно')
    time_create = models.DateTimeField(auto_now_add=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True, auto_now=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_complete = models.BooleanField(blank=True, default=False, verbose_name='Завершить задание')


    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])


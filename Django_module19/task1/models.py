from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя покупателя')
    balance = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Баланс')
    age = models.IntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название игры')
    cost = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')
    size = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Размер файла')
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games', verbose_name='Покупатель')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-cost']

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название поста')
    content = models.TextField(max_length=1000, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'




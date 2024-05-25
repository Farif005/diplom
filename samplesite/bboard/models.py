from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    image = models.ImageField(upload_to='images/', verbose_name='Фотография') 
    phone = models.IntegerField(null=True, blank=True, verbose_name='Номер телефона')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    views = models.PositiveIntegerField(default=0)


    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']




class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


# Create your models here.


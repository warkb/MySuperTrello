from django.db import models

# логин: admin
# пароль: trelloadmin

class Desc(models.Model):
    name = models.CharField(max_length=200, help_text='Имя доски')
    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

class Card(models.Model):
    text = models.TextField(help_text='Позиция на доске')
    data = models.DateTimeField(auto_now_add=True, help_text='Время создания')
    desc = models.ForeignKey(Desc, on_delete=models.CASCADE, help_text='Родительская доска')
    position = models.PositiveIntegerField(help_text='Позиция на доске')
    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

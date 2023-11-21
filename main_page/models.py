from django.db import models

class FilmModel(models.Model):
    GENRE = (
        ('Classic', 'Classic'),
        ('Sport', 'Sport')
    )
    title = models.CharField(max_length=100, verbose_name='Укажите название авто')
    country = models.CharField(max_length=100, verbose_name='Укажите название страны')
    image = models.ImageField(max_length=100, upload_to='auto/')
    genre = models.CharField(max_length=100, choices=GENRE)
    director = models.CharField(max_length=100, verbose_name='Укажите цену')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.country}'

    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Авто'


class Afisha(models.Model):
    film_title = models.CharField(max_length=100)
    time_watch = models.TimeField()
    area = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.film_title


class Slider(models.Model):
    slider = models.URLField()

    def __str__(self):
        return self.slider
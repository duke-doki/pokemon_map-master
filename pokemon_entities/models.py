from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(
        max_length=200, blank=True, verbose_name='Английское название'
    )
    title_jp = models.CharField(
        max_length=200, blank=True, verbose_name='Японское название'
    )
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    text = models.TextField(blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='next_evolutions',
        verbose_name='Эволюции'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name='покемон'
    )
    latitude = models.FloatField(
        verbose_name='Широта', null=True, blank=True
    )
    longitude = models.FloatField(
        verbose_name='Долгота', null=True, blank=True
    )
    appeared_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name='Дата появления'
    )
    disappeared_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name='Дата исчезновения'
    )
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

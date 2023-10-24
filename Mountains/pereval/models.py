from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'{self.latitude},{self.longitude},{self.height}'

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


LEVEL = [
    ('1a', '1A'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
    ('4a', '4А'),
    ('4b', '4Б'),
    ('5a', '5А'),
    ('5b', '5Б'),
    ('6a', '6А'),
    ('6b', '6Б')
]


class Level(models.Model):
    winter = models.CharField(max_length=2, choices=LEVEL, verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=2, choices=LEVEL, verbose_name='Лето', null=True, blank=True)
    autumn = models.CharField(max_length=2, choices=LEVEL, verbose_name='Осень', null=True, blank=True)
    spring = models.CharField(max_length=2, choices=LEVEL, verbose_name='Весна', null=True, blank=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

    class Meta:
        verbose_name = 'Уровень сложности перевала'
        verbose_name_plural = 'Уровни сложности перевала'


class Mountain(models.Model):
    STATUS = [
        ('new', 'новый'),
        ('pending', 'модератор взял в работу'),
        ('accepted', 'модерация прошла успешно'),
        ('rejected', 'модерация прошла, информация не принята'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    beautyTitle = models.CharField(max_length=255, verbose_name='Титульное название')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_titles = models.CharField(max_length=255, verbose_name='Альтернативное название')
    connect = models.TextField(verbose_name='Соединяет')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} {self.beautyTitle}'

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'


class Images(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE, related_name='images')

    data = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

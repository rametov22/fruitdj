from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse_lazy


class HomeModel(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('контент')
    is_active = models.BooleanField(default=False)
    images = models.ManyToManyField('Image')

    def __str__(self):
        return f"{self.title}{self.images}"


class Image(models.Model):
    img = models.ImageField('картинка', upload_to='home_images/')
    category = models.CharField('категория', max_length=20, default='fruits', choices=[('fruits', 'Fruits'), ('vegetables', 'Vegetables')])

    def __str__(self):
        return f"Image {self.pk}"


class FeaturesModel(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('Контент')
    icon = models.CharField(max_length=100, default='fas fa-car-side fa-3x text-white')

    def __str__(self):
        return self.title


class BannerModel(models.Model):
    title = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    content = models.TextField('контент')
    price = models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=2, max_digits=6)
    img = models.ImageField(upload_to='banner')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FeatursModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField('Контент')
    img = models.ImageField(upload_to='featurs')
    color = models.CharField(max_length=100, default='service-item bg-secondary rounded border border-secondary')
    color2 = models.CharField(max_length=100, default='service-content bg-primary text-center p-4 rounded')
    text = models.CharField(max_length=100, default='text-white')

    def __str__(self):
        return self.title


class CategoryModel(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField('контент')
    img = models.ImageField('img', upload_to='products/')
    price = models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=2, max_digits=6)
    is_exclusive = models.BooleanField(default=False)
    type = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    slug = models.SlugField('Slug', default='slug')
    weight = models.PositiveIntegerField(default=1)
    Country = models.CharField(default='uzb')
    Quality = models.CharField(default='organic')
    Check = models.CharField(default='healthy')
    MinWeight = models.PositiveIntegerField(default=1)
    STAR_CHOICES = [
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ]
    stars = models.IntegerField(choices=STAR_CHOICES, default=4)

    def __str__(self):
        return f'{self.name, self.type}'

    def get_absolute_url(self):
        return reverse_lazy('food_slug', kwargs={'pk': self.pk})


class BlogComments(models.Model):
    post = models.ForeignKey(ProductModel, related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField('Комментария')
    name = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    STAR_CHOICES = [
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ]
    stars = models.IntegerField(choices=STAR_CHOICES, default=0, verbose_name='оценка')
    to_feed_back = models.BooleanField(default='False', verbose_name='К главному')

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарии'
        ordering = ('-date_add',)

    def __str__(self):
        return f'{self.name} : "{self.comment[:50]}"'


class FactModel(models.Model):
    title = models.CharField(max_length=255)
    num = models.IntegerField(verbose_name='int')

    def __str__(self):
        return self.title


class ReviewModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField('email')
    text = models.TextField('text')
    date_created = models.DateTimeField(auto_now_add=True)
    STAR_CHOICES = [
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ]
    stars = models.IntegerField(choices=STAR_CHOICES, default=0, verbose_name='оценка')

    def __str__(self):
        return self.name






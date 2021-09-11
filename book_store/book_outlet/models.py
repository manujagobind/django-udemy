from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = 'Address'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    def full_name(self):
        return f"{self.last_name}, {self.first_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
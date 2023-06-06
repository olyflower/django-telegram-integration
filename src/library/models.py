from django.db import models
from faker import Faker


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="book/", blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(
                title=faker.word(),
                author=faker.name(),
                description=faker.sentence(),
            )

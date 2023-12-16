from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категории')
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name="sub_categoryies")

    def __str__(self):
        if self.sub_category:
            return f"{self.name}-->{self.sub_category}"
        return f"{self.name}"

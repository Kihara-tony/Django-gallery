from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    def save_category(self):
        self.save()
    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()
    def update_category(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

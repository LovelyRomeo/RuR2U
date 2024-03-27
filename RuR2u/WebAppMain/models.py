from django.db import models

# Create your models here.

class Category(models.Model):
    CategoryName = models.CharField('Название категории', max_length=70)
    
    
    def __str__(self):
        return self.CategoryName
    
    class Meta:
        verbose_name='Категории'
        verbose_name_plural='Категории'
    
class Elements(models.Model):
    Categoryselect = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    ElementPhoto = models.ImageField("Фото элемента", upload_to='elphoto/')
    ElementDate = models.DateField("Дата")
    ElementName = models.CharField("Название статьи", max_length=100)
    PagePhoto = models.ImageField("Фото страницы", upload_to='mainphoto/')
    PageText = models.TextField("Основной текст статьи")
    
    def __str__(self):
        return self.ElementName
    
    class Meta:
        verbose_name='Наполнение'
        verbose_name_plural='Наполнение'
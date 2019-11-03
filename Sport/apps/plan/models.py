from django.db import models



class City(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name		


class MainContent(models.Model):
	title = models.CharField('Название',max_length=45)
	article_content = models.TextField('Текст')
	mc_image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name= 'Изображение',)

	def __str__(self):
		return self.title
	

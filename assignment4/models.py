from __future__ import unicode_literals

from django.db import models

from tinymce import models as tinymcemodels


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')

class Article(Content):
	text = tinymcemodels.HTMLField()

### The Image model should (additionally) have:


class Image(Content):
    path = models.CharField(max_length=500)

    def info(self): 
    	return "%s, %s, %s, %s" % (self.title, self.subtitle, self.contributors, self.pub_date)

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def die(self): 
    	die = self.delete() 




# Create your models here.

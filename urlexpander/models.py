from django.db import models
from django.core.urlresolvers import reverse


class URL(models.Model):
	origin = models.URLField()	
	dest = models.URLField()
	status = models.IntegerField()
	title = models.CharField(max_length=100)
	
	def getExpanded(self):
		return reverse('urlexpander:url_detail)', kwargs={'pk': self.pk})

    




from django.db import models

class Recipient(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    family_relationship = models.CharField(
            max_length=200, default="#davethecat's third-favorite",
            blank=True, null=True)
    personalized_greeting = models.CharField(
            max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "recipients"

    def __unicode__(self):
        return self.first_name

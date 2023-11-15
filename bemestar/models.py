from django.db import models

class bemestar(models.Model):

    image_src = models.TextField()
    post_url = models.TextField()

    class Meta:
        managed = False
        db_table = "entities_entity"


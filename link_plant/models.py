from django.db import models

# Create your models here.

# We need two tables : Profile table and Links table

class Profile(models.Model):
    # name, slug, bg_color
    BG_CHOICES = (
        ('blue','Blue'),
        ('green','Green'),
        ('yellow','Yellow'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.name
    
class Link(models.Model):
    # text, url, profile
    text =models.CharField(max_length=100)
    url =models.URLField()
    # This is how to create a relation many to one --> By using foreign key
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links") # on_delete--> when I delete the profile the links should be deleted as well

    def __str__(self):
        return f" {self.text} : {self.url}"
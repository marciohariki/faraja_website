from django.db import models

# Create your models here.

class Trustee(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    
    def __unicode__(self):
        return self.name
    
class Therapist(models.Model):
    name = models.CharField(max_length=256)
    picture = models.FileField(upload_to='files')
    text = models.TextField()
    
    def __unicode__(self):
        return self.name    
    
class WhoWeAre(models.Model):
    text = models.TextField()
    
    def __unicode__(self):
        return "Edit the text here!"
    
class WhatWeDo(models.Model):
    text = models.TextField()
    
    def __unicode__(self):
        return "Edit the text here!"

class WhatWeDoActivity(models.Model):
    name = models.CharField(max_length=256)
    preview_text = models.TextField()
    text = models.TextField()
    
    def __unicode__(self):
        return self.name

class Involved(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    phone = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class CancerTreatment(models.Model):
    institution = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    obs = models.CharField(max_length=512, blank=True, null=True)
    
    def __unicode__(self):
        return self.institution
    

class CancerSpecific(models.Model):
    name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=256)
    picture = models.FileField(upload_to='files')
    text = models.TextField()
    
    def __unicode__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    def __unicode__(self):
        return self.question    
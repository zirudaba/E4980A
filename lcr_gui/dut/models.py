from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField('Project Created on')
    status = models.CharField(max_length=30)
    comments = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return self.title
    
class Dut(models.Model):

    DUT_TYPE_CHOICES = (
        ('Prot', 'Prototype'),
        ('Prod', 'Product'),
        ('Comp', 'Component'),    
    )    
    
    project = models.ForeignKey(Project)
    dut_type = models.CharField(max_length=4, choices=DUT_TYPE_CHOICES)
    name = models.CharField(max_length=80)
    sn = models.SlugField(max_length=20, unique=True)
    def __unicode__(self):
        return self.dut_type
        
class MeasurementSetup(models.Model):
    
    FREQ_MODE_CHOICES = (
        ('SF', 'Single Frequency'),
        ('MF', 'Frequency Sweep'),    
    )    
    
    dut = models.ForeignKey(Dut)
    measured_param = models.CharField(max_length=3)
    freq_mode = models.CharField(max_length=2, choices=FREQ_MODE_CHOICES)
    freq_single = models.FloatField()
    freq_lowlim = models.FloatField()
    freq_upplim = models.FloatField()
    level_volt = models.FloatField()
    level_amp = models.FloatField()
    bandsize = models.IntegerField(default=10)
    acl = models.BooleanField(default=False)
    def __unicode__(self):
        return self

class Results(models.Model):
    meas_setup = models.ForeignKey(MeasurementSetup)
    freq = models.FloatField()
    param_1 = models.FloatField()
    param_2 = models.FloatField()
    meas_stat = models.FloatField()
    date_tested = models.DateTimeField('Tested on')
    def __unicode__(self):
        return self
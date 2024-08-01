from django.db import models

# Create your models here.    
class Methodology(models.Model):
    libray_module_import=models.TextField(max_length=1000)
    column_drop=models.TextField(max_length=1000)
    preprocessing=models.TextField(max_length=1000)
    stemming=models.TextField(max_length=1000)
    
    class Meta:
        verbose_name="Methodology"
        verbose_name_plural="Methodologies"
        
class Report(models.Model):
    introduction=models.TextField(max_length=500)
    objective=models.TextField(max_length=200)
    motivation=models.TextField(max_length=500)
    project_overview=models.TextField(max_length=1000)
    report_methodology=models.ForeignKey(Methodology,on_delete=models.CASCADE,related_name="methodlogies",default="")
    discussion=models.TextField(max_length=1000)
    conclusion=models.TextField(max_length=1000)
    title=models.CharField(max_length=100)
    intial_line=models.CharField(max_length=50)
    references=models.URLField()
    project_links=models.URLField()
    
    class Meta:
        verbose_name_plural="Report"
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
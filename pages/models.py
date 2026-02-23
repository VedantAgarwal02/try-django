from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name        = models.CharField(max_length=40)
    email       = models.EmailField()
    subject     = models.CharField(max_length=200)
    message     = models.TextField(max_length=2000)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

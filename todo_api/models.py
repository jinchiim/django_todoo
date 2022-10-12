from tabnanny import verbose
from django.db import models

class Todo(models.Model):
    title = models.CharField(
        max_length=100, 
        verbose_name = '할 일', )
    description = models.TextField(
        verbose_name = '세부 사항'
    )
    due_date = models.DateTimeField(
        null=True,
        verbose_name = '마감 기한',
        help_text = '마감 기한을 선택해 주세요.'
        )
    completed = models.BooleanField(
        verbose_name = '완료 여부',
        default=False)
        
        
    def __str__(self):
        return self.title
    

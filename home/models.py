from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Authority(models.Model):
    names = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    charges=models.IntegerField(default='Free')
    photo = models.ImageField(upload_to='authority_photos/', null=True, blank=True)
    specialization = models.CharField(max_length=100,null=True)
    years_of_experience = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.names} -{self.location}'




class Case(models.Model):
    CASE_TYPES = [
    ('Corruption', 'Corruption'),
    ('Accident', 'Accident'),
    ('Harassment', 'Harassment'),
    ('Sexual Abuse', 'Sexual Abuse'),
    ('Discrimination', 'Discrimination'),      
    ('Domestic Violence', 'Domestic Violence'),
    ('Child Abuse', 'Child Abuse'),             
    ('Fraud', 'Fraud'),                         
    ('Workplace Misconduct', 'Workplace Misconduct'), 
    ('Cyber Crime', 'Cyber Crime'),             
    ('Human Trafficking', 'Human Trafficking'), 
    ('Environmental Crime', 'Environmental Crime'), 
    ('Bullying', 'Bullying'),                   
    ('Police Brutality', 'Police Brutality'),   
    ('Drug Trafficking', 'Drug Trafficking'), 
    ('Land Dispute', 'Land Dispute'),
    ('Tax Evasion', 'Tax Evasion'),
    ('Identity Theft', 'Identity Theft'),
    ('Property Damage', 'Property Damage'),
    ('Fraudulent Financial Institution', 'Fraudulent Financial Institution'),
    ('Terrorism', 'Terrorism'),
    ('Vandalism', 'Vandalism'),
    ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='cases')
    case_type = models.CharField(max_length=50, choices=CASE_TYPES)
    description = models.TextField()
    anonymous_name = models.CharField(max_length=100,null=True)
    anonymous_email = models.EmailField(null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    attachment = models.FileField(upload_to='case_attachments/', null=True, blank=True)  # File upload field
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15,null=True)
    location = models.CharField(max_length=100,null=True)
    tracked_by = models.ManyToManyField(User, related_name='tracked_cases', blank=True)
    assigned_to = models.ForeignKey(Authority,on_delete=models.SET_NULL,null=True,blank=True)



class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    lawyer = models.ForeignKey(Authority, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lawyer']

    def __str__(self):
        return f"Conversation between {self.user.username} and {self.lawyer}"
    

class Comment(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='comments')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=100,null=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.sender.username} in conversation with {self.conversation.lawyer}"
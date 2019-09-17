from django.db import models

# Create your models here.
class Opprtunity(models.Model):
    STATUS_CHOICES=(('choose','Choose'),('full_time','Full_Time'),('part_time','Part_Time'))
    Job_Type=models.CharField(max_length=40,choices=STATUS_CHOICES,default='choose')
    STATUS_CHOICES=(('choose','Choose'),('python_developer','Python_Developer'),('web_developer','Web_Developer'),('javascript_developer','JavaScript_Developer'),('ai','AI'),('machine_learning','Machine_Learning'))
    Posting_title=models.CharField(max_length=40,choices=STATUS_CHOICES,default='choose')
    Date_opened=models.DateField()
    STATUS_CHOICES=(('choose','Choose'),('hyderabad','Hyderabad'),('bangalore','Bangalore'),('kolkata','Kolkata'),('bhubaneswar','Bhubaneswar'))
    city=models.CharField(max_length=40,choices=STATUS_CHOICES,default='choose')





class BasicInfo(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    STATUS_CHOICES=(('choose','Choose'),('bangalore','Bangalore'),('odisha','Odisha'),('hyderabad','Hyderabad'),('pune','Pune'))
    your_location=models.CharField(max_length=10,choices=STATUS_CHOICES,default='choose')
    current_address=models.CharField(max_length=64)
    STATUS_CHOICES=(('choose','Choose'),('hindi','Hindi'),('english','English'))
    language=models.CharField(max_length=10,choices=STATUS_CHOICES,default='choose')
    STATUS_CHOICES=(('choose','Choose'),('india','India'),('us','US'),('japan','Japan'),('austrelia','Austrelia'))
    Nationality=models.CharField(max_length=10,choices=STATUS_CHOICES,default='choose')
    STATUS_CHOICES=(('choose','Choose'),('bca','BCA'),('mca','MCA'),('btech','BTECH'))
    qualification=models.CharField(max_length=10,choices=STATUS_CHOICES,default='choose')
    STATUS_CHOICES=(('choose','Choose'),('2019','2019'),('2018','2018'),('2017','2017'),('2016','2016'))
    year_of_passout=models.CharField(max_length=10,choices=STATUS_CHOICES,default='choose')
    DOB=models.DateField()
    workingexpfrom=models.DateField()
    workingexpto=models.DateField()
    STATUS_CHOICES=(('choose','Choose'),('full_time','Full_Time'),('part_time','Part_Time'))
    Job_Type=models.CharField(max_length=10,choices=STATUS_CHOICES,default='choose')

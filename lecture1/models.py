from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField()
    empname = models.CharField(max_length=20)
    empsalary = models.IntegerField()
    empaddress = models.CharField(max_length=50)
    class Meta:
        db_table = "my_employee"
    # def __str__(self) -> str:
    #     return super().__str__()

    def __str__(self):
        return self.empname



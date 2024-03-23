from django.db import models

class Person(models.Model):
    first_name = models.CharField('Student first name', max_length=100)
    last_name = models.CharField('Student last name', max_length=100, blank=True)
    dob = models.DateTimeField('Student date of birth', null=True, blank=True)
    email = models.EmailField('Student email', null=True, blank=True)
    address = models.CharField('Student address', max_length=300, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    student_id = models.CharField('Student ID', max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    course_code = models.CharField('Course code', max_length=100)
    course_name = models.CharField('Course name', max_length=100)
    credits = models.PositiveIntegerField('Number of credits', null=True, blank=True)
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"
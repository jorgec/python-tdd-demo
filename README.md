# TDD Demo
## Room Management System

### Specifications
A room has:
+ Some form of identifier
+ Variable capacity
+ Can only be scheduled by one class at any given time

A class has:
+ A subject
+ A schedule
+ A room
+ A teacher
+ At most 30 unique students

A subject has:
+ A name
+ Variable number of units
+ Any number of classes

A student has:
+ At least 1 class
+ Can’t have more than 1 class with the same subject
+ Can’t exceed 24 units in one semester

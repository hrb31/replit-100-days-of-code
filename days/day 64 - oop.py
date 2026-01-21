## object oriented programming

class job:
  name = None
  salary = None
  hours_worked = None

  def __init__(self, name, salary, hours_worked):
    self.name = name
    self.salary = salary
    self.hours_worked = hours_worked

  def print_details(self):
    print("Name:", self.name)
    print("Salary:", self.salary)
    print("Hours Worked:", self.hours_worked)

class doctor(job):
  speciality = None
  experience = None

  def __init__(self, speciality, experience):
    self.name = "Doctor"
    self.salary = 90000
    self.hours_worked = 50
    self.speciality = speciality
    self.experience = experience

  def print_details(self):
    print("Name:", self.name)
    print("Salary:", self.salary)
    print("Hours Worked:", self.hours_worked)
    print("Speciality:", self.speciality)
    print("Years of Experience:", self.experience)

class teacher(job):
  subject = None
  position = None

  def __init__(self, subject, position):
    self.name = "Teacher"
    self.salary = 40000
    self.hours_worked = 40
    self.subject = subject
    self.position = position

  def print_details(self):
    print("Name:", self.name)
    print("Salary:", self.salary)
    print("Hours Worked:", self.hours_worked)
    print("Position:", self.position)

lawyer = job("Lawyer", 50000, 45)
lawyer.print_details()
print()
pediatric = doctor("Pediatric Doctor", 7)#
pediatric.print_details()
print()
compsci = teacher("Computer Science", "Classroom Teacher")
compsci.print_details()

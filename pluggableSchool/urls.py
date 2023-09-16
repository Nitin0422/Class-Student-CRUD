from django.urls import path
from . import views

app_name="pluggableSchool"
urlpatterns = [
    path('', views.index, name="index"),
    path('class/<int:class_id>', views.showStudents, name="showStudents"),
    path('addClass/', views.addClass, name="addClass"),
    path('<int:class_id>/addStudent/', views.addStudent, name='addStudent'),
    path('student/<int:student_id>/<int:class_id>', views.editStudent, name = "editStudent"),
    path('class/edit/<int:class_id>', views.editClass, name="classDetails"),
    path('class/delete/<int:class_id>', views.deleteClass, name="deleteClass"),
    path('student/delete/<int:student_id>', views.deleteStudent, name="deleteStudent")
]
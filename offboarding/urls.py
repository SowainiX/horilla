"""
offboarding/urls.py

This module is used to register url mappings to functions
"""
from django.urls import path
from offboarding import views

urlpatterns = [
    path("offboarding-pipeline", views.pipeline, name="offboarding-pipeline"),
    path("create-offboarding", views.create_offboarding, name="create-offboarding"),
    path("delete-offboarding", views.delete_offboarding, name="delete-offboarding"),
    path(
        "create-offboarding-stage", views.create_stage, name="create-offboarding-stage"
    ),
    path("add-employee", views.add_employee, name="add-employee"),
    path(
        "delete-offboarding-stage", views.delete_stage, name="delete-offboarding-stage"
    ),
    path(
        "offboarding-change-stage", views.change_stage, name="offboarding-change-stage"
    ),
    path("view-offboarding-note", views.view_notes, name="view-offboarding-note"),
    path("add-offboarding-note", views.add_note, name="add-offboarding-note"),
    path(
        "delete-note-attachment", views.delete_attachment, name="delete-note-attachment"
    ),
    path("offboarding-add-task", views.add_task, name="offboarding-add-task"),
    path("update-task-status", views.update_task_status, name="update-task-status"),
    path("offboarding-assign-task", views.task_assign, name="offboarding-assign-task"),
     path("delete-offboarding-employee",views.delete_employee,name="delete-offboarding-employee"),
     path("delete-offboarding-task",views.delete_task,name="delete-offboarding-task"),
]
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Task, COMPLETE, NOT_COMPLETE


@receiver(post_save, sender=Task)
def update_tasklist_status(sender, instance, created, **kwargs):
    task_list = instance.task_list
    is_completed = True
    for task in task_list.tasks.all():
        if task.status != COMPLETE:
            is_completed = False
            break
    task_list.status = COMPLETE if is_completed else NOT_COMPLETE
    task_list.save()


@receiver(post_save, sender=Task)
def update_house_point(sender, instance, created, **kwargs):
    house = instance.task_list.house
    if instance.status == COMPLETE:
        house.points += 5

    elif instance.status == NOT_COMPLETE:
        if house.points >= 5:
            house.points -= 5
    house.save()


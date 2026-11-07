from datetime import date

from django.db import models
from django.contrib.auth.models import User


class TodoQuerySet(models.QuerySet):
    def for_user(self, user: User):
        return self.filter(user=user)


class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Prazo", null=True, blank=True)
    finished_at = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = [models.F("deadline").asc(nulls_last=True), "-created_at"]

    def mark_as_finished(self) -> None:
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
    
    objects = TodoQuerySet.as_manager()

    def __str__(self) -> str:
        return self.title


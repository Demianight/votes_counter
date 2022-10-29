from django.db import models


class Candidate(models.Model):
    name = models.CharField(
        max_length=50,
    )
    votes = models.IntegerField(
        default=0,
    )

    def __str__(self) -> str:
        return self.name

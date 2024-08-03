from django.db import models


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    return_date = models.DateField()
    departure_date = models.DateField()
    number_of_travelers = models.IntegerField()
    creater_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Trip to {self.destination} untill {self.return_date} with {self.number_of_travelers} traveler" + (
            's.' if self.number_of_travelers > 1 else '.'
            )
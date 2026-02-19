from djongo import models


class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24, null=True)
    is_superhero = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    user_id = models.CharField(max_length=24)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.user_id} - {self.type}"


class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    team_id = models.CharField(max_length=24)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team_id} - {self.points} points"

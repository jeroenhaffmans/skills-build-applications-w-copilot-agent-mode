from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(id='t1', name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(id='t2', name='Test Team2', description='desc')
        user = User.objects.create(id='u1', name='Test User', email='test@example.com', team_id=team.id, is_superhero=True)
        self.assertEqual(str(user), 'Test User')

    def test_activity_create(self):
        team = Team.objects.create(id='t3', name='Test Team3', description='desc')
        user = User.objects.create(id='u2', name='Test User2', email='test2@example.com', team_id=team.id, is_superhero=False)
        activity = Activity.objects.create(id='a1', user_id=user.id, type='Run', duration=30, date='2024-01-01')
        self.assertEqual(str(activity), 'u2 - Run')

    def test_workout_create(self):
        workout = Workout.objects.create(id='w1', name='Test Workout', description='desc', suggested_for='All')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_create(self):
        team = Team.objects.create(id='t4', name='Test Team4', description='desc')
        leaderboard = Leaderboard.objects.create(id='l1', team_id=team.id, points=10)
        self.assertEqual(str(leaderboard), 't4 - 10 points')

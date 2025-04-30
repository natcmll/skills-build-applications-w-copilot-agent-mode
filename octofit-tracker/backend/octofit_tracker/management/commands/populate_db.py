from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
        user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

        # Create test activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30)
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45)

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        # Create test workouts
        Workout.objects.create(name="Workout A", description="A sample workout")

        # Additional test users
        user3 = User.objects.create(email="user3@example.com", name="User Three", password="password3")
        user4 = User.objects.create(email="user4@example.com", name="User Four", password="password4")

        # Additional test teams
        team2 = Team.objects.create(name="Team Beta", members=[user3.id, user4.id])

        # Additional test activities
        Activity.objects.create(user=user3, activity_type="Swimming", duration=60)
        Activity.objects.create(user=user4, activity_type="Hiking", duration=120)

        # Additional test leaderboard entries
        Leaderboard.objects.create(team=team2, score=200)

        # Additional test workouts
        Workout.objects.create(name="Workout B", description="Another sample workout")
        Workout.objects.create(name="Workout C", description="Yet another sample workout")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))

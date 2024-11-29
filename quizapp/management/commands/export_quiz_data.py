# cms/quizapp/management/commands/export_quiz_data.py
from django.core.management.base import BaseCommand
from quizapp.models import Quiz
import json

class Command(BaseCommand):
    help = 'Export all quiz data'

    def handle(self, *args, **options):
        # Retrieve all Quiz instances
        quizzes = Quiz.objects.all()

        # Create a list to store exported data
        exported_data = []

        # Loop through each Quiz instance and export its data
        for quiz in quizzes:
            data = {
                'id': quiz.id,  # Include the primary key id
                'title': quiz.title,
                'quiz_type': quiz.quiz_type,
                'data': quiz.data,
                'created_at': quiz.created_at.isoformat(),  # Include creation timestamp
                'last_modified': quiz.last_modified.isoformat(),  # Include last modified timestamp
            }
            exported_data.append(data)

        # Write exported data to a JSON file with proper indentation
        with open('exported_quiz_data.json', 'w') as f:
            json.dump(exported_data, f, indent=4)  # Indent with 4 spaces

        self.stdout.write(self.style.SUCCESS('Quiz data exported successfully.'))

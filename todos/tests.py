from datetime import date, timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm


class TodoModelAndFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="securepassword123")

    def test_create_todo_with_deadline(self):
        tomorrow = date.today() + timedelta(days=1)
        todo = Todo.objects.create(
            title="Tarefa com prazo",
            deadline=tomorrow,
            user=self.user,
        )
        self.assertEqual(todo.deadline, tomorrow)
        self.assertEqual(str(todo), "Tarefa com prazo")

    def test_create_todo_without_deadline(self):
        todo = Todo.objects.create(
            title="Tarefa sem prazo",
            deadline=None,
            user=self.user,
        )
        self.assertIsNone(todo.deadline)
        self.assertEqual(str(todo), "Tarefa sem prazo")

    def test_todo_ordering_nulls_last(self):
        future_date = date.today() + timedelta(days=5)
        near_date = date.today() + timedelta(days=1)

        todo_null = Todo.objects.create(title="Sem prazo", deadline=None, user=self.user)
        todo_near = Todo.objects.create(title="Prazo perto", deadline=near_date, user=self.user)
        todo_future = Todo.objects.create(title="Prazo longe", deadline=future_date, user=self.user)

        ordered = list(Todo.objects.for_user(self.user))
        self.assertEqual(ordered[0], todo_near)
        self.assertEqual(ordered[1], todo_future)
        self.assertEqual(ordered[2], todo_null)

    def test_todo_form_has_date_widget(self):
        form = TodoForm()
        self.assertEqual(form.fields["deadline"].widget.input_type, "date")
        self.assertFalse(form.fields["deadline"].required)

    def test_todo_form_valid_without_deadline(self):
        form = TodoForm(data={"title": "Comprar pão", "deadline": ""})
        self.assertTrue(form.is_valid())
        todo = form.save(commit=False)
        self.assertIsNone(todo.deadline)

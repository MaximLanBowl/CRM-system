from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .forms import *
from .models import Task
from django.utils.safestring import mark_safe
from datetime import datetime
from calendar import HTMLCalendar, Calendar
import logging

log = logging.getLogger(__name__)


class TaskListView(ListView):
    template_name = 'tasks/tasks-list.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/tasks-create.html'
    success_url = reverse_lazy('tasks:list')
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:list")
    template_name = 'tasks/task-delete.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/tasks-detail.html'
    context_object_name = "task"


class TaskUpdateView(UpdateView):
    template_name = "tasks/task-edit.html"
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse(
            "tasks:details",
            kwargs={"pk": self.object.pk},
        )


class Calendar(HTMLCalendar):

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, tasks):
        tasks_per_day = tasks.filter(date__day=day)
        d = ''
        for task in tasks_per_day:
            d += f'<li>{task.title} - {task.time}</li>'
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, tasks):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, tasks)
        return f'<tr>{week}</tr>'

    def formatmonth(self, tasks):
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=True)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, tasks)}\n'
        return cal


def calendar_view(request, year=datetime.now().year, month=datetime.now().month):
    tasks = Task.objects.all()
    cal = Calendar(year, month)
    html_cal = cal.formatmonth(tasks)
    return render(request, 'tasks/calendar.html', {'calendar': mark_safe(html_cal), 'year': year, 'month': month})


def tasks_report(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_report.html', {'tasks': tasks})

from calendar import HTMLCalendar as _HTMLCalendar

from django.utils.safestring import mark_safe

from ophrys.utils.views import MonthArchiveView, CreateView, DetailView, UpdateView, DeleteView

from .models import Event


class Calendar(MonthArchiveView):
    """
    View to show one month of the calendar with the events in it.
    """
    model = Event
    date_field = 'begin'
    month_format = '%m'
    allow_empty = True
    allow_future = True
    template_name = 'calendarevent/calendar.html'

    def get_context_data(self, *args, **kwargs):
        """
        Inserts the HTML calendar into the template context.
        """
        context = super().get_context_data(*args, **kwargs)
        context['html_calendar'] = mark_safe(HTMLCalendar(view_instance=self).formatmonth(int(self.get_year()), int(self.get_month())))
        return context


class HTMLCalendar(_HTMLCalendar):
    """
    Class for a calendar displayed as html table.
    """
    def __init__(self, view_instance, *args, **kwargs):
        self.view_instance = view_instance
        return super().__init__(*args, **kwargs)

    def formatday(self, day, weekday):
        """
        Returns a day as a table cell.

        Copied from the calendar module.
        """
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%s</td>' % (self.cssclasses[weekday], self.get_day_content(day))

    def get_day_content(self, day):
        event_list = []
        for event in self.view_instance.object_list:  # Check whether there is another var than object_list
            if event.begin.day == day:
                event_list.append(
                    '<a href="%(url)s">%(title)s</a>' % {'title': event.title,
                                                         'url': event.get_absolute_url()})
        return '%d %s' % (day, ' '.join(event_list))


class EventCreate(CreateView):
    model = Event


class EventDetail(DetailView):
    model = Event


class EventUpdate(UpdateView):
    model = Event


class EventDelete(DeleteView):
    model = Event
    success_url_name = 'calendar_default'

from ophrys.utils.views import DetailView

from .models import Event


class EventDetail(DetailView):
    model = Event

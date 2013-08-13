from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, UpdateView, MonthArchiveView
from django.views.generic import DeleteView as _DeleteView


class DeleteView(_DeleteView):
    """
    View to delete objects. You have to provide the argument 'success_url_name'
    instead of the argument 'success_url'.
    """
    def get_success_url(self):
        return reverse(self.success_url_name)

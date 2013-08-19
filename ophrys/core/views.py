from django import forms

from ophrys.utils.views import FormView

from .config import config
from .signals import get_config_groups


class ConfigView(FormView):
    """
    The view for the config page.
    """
    form_class = forms.Form
    success_url = '#'
    template_name = 'core/config_form.html'

    def __init__(self, *args, **kwargs):
        """
        Gets all config groups and links them to this view.
        """
        return_value = super().__init__(*args, **kwargs)
        self.config_groups = [group for receiver, group in get_config_groups.send(sender='config_view_class')]
        return return_value

    def get_form(self, *args, **kwargs):
        """
        Gets the form for the view. Includes all form fields given by the
        config groups.
        """
        form = super().get_form(*args, **kwargs)
        for key, field in self.generate_all_form_fields():
            form.fields[key] = field
        return form

    def generate_all_form_fields(self):
        """
        Generates the fields for the get_form() function.
        """
        for config_group in self.config_groups:
            for variable in config_group:
                yield (variable.key, variable.form_field)

    def get_initial(self):
        """
        Returns a dictonary with the actual values of the config variables
        as intial value for the form.
        """
        initial = super().get_initial()
        for key, field in self.generate_all_form_fields():
            initial.update({key: getattr(config, key)})
        return initial

    def form_valid(self, form):
        """
        Saves all data of a valid form.
        """
        for key in form.cleaned_data:
            setattr(config, key, form.cleaned_data[key])
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        """
        Adds all groups objects to the template context.
        """
        context = super().get_context_data(*args, **kwargs)
        context['config_groups'] = self.config_groups
        return context

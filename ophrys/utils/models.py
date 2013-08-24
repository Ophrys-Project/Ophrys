from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models

from .views import ListView, CreateView, DetailView, UpdateView, DeleteView


class GetAbsoluteUrlMixin:
    """
    Mixin to add the methods get_absolute_url() and get_absolute_url_name()
    to a model class. These methods look for an url name in the nested
    namespace. The top level namespace is the name of the application
    (including the name of the project), e. g. `yourproject.yourapp`. The
    low level namespace is the name of the current model (class), e. g.
    `YourModel`. The url name can be something like `list`, `create`,
    `detail`, `update` or `delete`. So this mixin tries to reverse e. g.
    `yourproject.yourapp:YourModel:detail`. The named urls except `list`
    and `create` have to accept either a pk argument or a slug argument.
    """
    def get_absolute_url(self, url_name='detail'):
        """
        Returns the url concerning the given url name. The url must accept
        a pk argument or a slug argument if its name is not `list` or
        `create`.
        """
        if url_name == 'list' or url_name == 'create':
            return reverse(self.get_absolute_url_name(url_name))
        try:
            return reverse(self.get_absolute_url_name(url_name), kwargs={'pk': str(self.pk)})
        except NoReverseMatch:
            pass
        # TODO: Raise an specific error message if self.slug does not exist or
        #       reverse does not find an url.
        return reverse(self.get_absolute_url_name(url_name), kwargs={'slug': str(self.slug)})

    def get_absolute_url_name(self, url_name='detail'):
        """
        Returns the full url name (including namespace patterns) of the
        given url name.
        """
        project_app_name = type(self).__module__.split('.models')[0]
        class_name = type(self).__name__
        return '%s:%s:%s' % (project_app_name, class_name, url_name)


class AutoModelMixin(GetAbsoluteUrlMixin):
    """
    Mixin for models to add automaticly designed urls and views.

    Add this mixin to your model and include YourModel().urls in the
    urlpatterns of your application::

      url(r'^example/', include(YourModel().urls))

    The urls and classes for a list view (`/example/`), a create view
    (`/example/create/`), a detail view (`/example/<pk>/`), an update view
    (`/example/<pk>/update/`) and a delete view (`/example/<pk>/delete/`)
    will be setup. You only have to write the corresponding templates with
    Django's default template names (`yourapp/yourmodel_list.html`,
    `yourapp/yourmodel_form.html`, `yourapp/yourmodel_detail.html`,
    `yourapp/yourmodel_confirm_delete.html`).

    The GetAbsoluteUrlMixin is used, so you have to set the inclusion of the
    urls into a specific top level namespace concerning to the name of the
    application (including the name of the project)::

      url(r'^example_app/', include(yourproject.yourapp.urls), namespace='yourproject.yourapp')
    """
    @property
    def urls(self):
        """
        Attribute of mixed models. Include this in the urlpatterns of
        your application::

          url(r'^example/', include(YourModel().urls))
        """
        return (self.get_urlpatterns(), None, type(self).__name__)

    def get_urlpatterns(self):
        """
        Method to get the urlpatterns object. Override this method to
        customize the urls.
        """
        return patterns(
            '',
            url(r'^$', self.get_view_class('List').as_view(), name='list'),
            url(r'^create/$', self.get_view_class('Create').as_view(), name='create'),
            url(r'^(?P<pk>\d+)/$', self.get_view_class('Detail').as_view(), name='detail'),
            url(r'^(?P<pk>\d+)/update/$', self.get_view_class('Update').as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', self.get_view_class('Delete').as_view(), name='delete'))

    def get_view_class(self, view_name):
        """
        Method to construct the view classes. Override this method to
        customize them.
        """
        view_class_definitions = {'model': type(self)}
        if view_name == 'List':
            view_class = ListView
        elif view_name == 'Create':
            view_class = CreateView
        elif view_name == 'Detail':
            view_class = DetailView
        elif view_name == 'Update':
            view_class = UpdateView
        elif view_name == 'Delete':
            view_class = DeleteView
            view_class_definitions['success_url_name'] = self.get_absolute_url_name('list')
        else:
            raise ValueError('The view name "%s" is unknown.' % view_name)
        return type(view_name, (view_class,), view_class_definitions)

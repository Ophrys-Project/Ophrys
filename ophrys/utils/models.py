from django.core.urlresolvers import reverse, NoReverseMatch


class GetAbsoluteUrlMixin(object):
    """
    Mixin to add the method get_absolute_url() to a model class. The method
    looks for an url name matching to the current model and the given
    url_name like 'detail', 'update' or 'delete'.
    """
    def get_absolute_url(self, url_name='detail'):
        module_name = type(self).__module__.split('.models')[0]
        class_name = type(self).__name__
        try:
            return reverse('%s:%s:%s' % (module_name, class_name, url_name),
                           kwargs={'pk': str(self.pk)})
        except NoReverseMatch:
            pass
        # TODO: Raise an specific error message if self.slug does not exist or
        #       reverse does not find an url.
        return reverse('%s:%s:%s' % (module_name, class_name, url_name),
                       kwargs={'slug': str(self.slug)})

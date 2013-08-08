from django.core.urlresolvers import reverse, NoReverseMatch


class GetAbsoluteUrlMixin(object):
    def get_absolute_url(self, url_name='detail'):
        class_name = type(self).__name__
        module_name = type(self).__module__
        try:
            return reverse('%s.%s.%s' % (module_name, class_name, url_name),
                           kwargs={'pk': str(self.pk)})
        except NoReverseMatch:
            pass
        # TODO: Raise an specific error message if self.slug does not exist or
        #       reverse does not find an url.
        return reverse('%s.%s.%s' % (module_name, class_name, url_name),
                       kwargs={'slug': str(self.slug)})

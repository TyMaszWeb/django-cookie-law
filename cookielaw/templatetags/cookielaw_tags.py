from classytags.helpers import InclusionTag
from django import template
from django.template.loader import render_to_string


register = template.Library()


class CookielawBanner(InclusionTag):
    """
    Displays cookie law banner only if user has not dismissed it yet.
    """

    template = 'cookielaw/banner.html'

    def render_tag(self, context, **kwargs):
        template = self.get_template(context, **kwargs)
        if context['request'].COOKIES.get('cookielaw_accepted', False):
            return ''
        data = self.get_context(context, **kwargs)
        return render_to_string(template, data, context_instance=context)

register.tag(CookielawBanner)

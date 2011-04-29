from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.context_processors import csrf


def main(request):
    doc = {'text':_('This text (maybe) will be translated'),}
    return render_to_response('main/template.html', {
                              'doc': doc, },
                              context_instance=RequestContext(request))

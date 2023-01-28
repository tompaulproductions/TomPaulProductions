from django.template.response import TemplateResponse


def home_view(request):
    context_data = {

    }
    return TemplateResponse(request, template='landing/core/base/base.html', context=context_data)

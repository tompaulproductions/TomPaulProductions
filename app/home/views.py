from django.template.response import TemplateResponse


def home_view(request):
    context_data = {}
    return TemplateResponse(request, template='home/home_page.html', context=context_data)

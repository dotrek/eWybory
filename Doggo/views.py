from django.http import HttpResponse


# Create your views her

def details(request, kandydat_id):
    return HttpResponse("Details of: " % kandydat_id)


def results(request, kandydat_id):
    return HttpResponse("Result for: " % kandydat_id)

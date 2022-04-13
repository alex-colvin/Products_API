from rest_framework import api_view
from rest_framework import Response

api_view(['GET'])
def products_list(request):

    return Response('ok')
    
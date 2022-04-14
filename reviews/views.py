from rest_framework import generics
from .serializers import ReviewSerializer
from .models import Review
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ReviewsList(APIView):

    def get(self, request):    
        if request.method == 'GET':
            reviews = Review.objects.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetail(APIView):

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reviews = Review.objects.filter(product_id=pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET','POST'])
# def reviews_list(request):
    
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=200)

#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid() == True:
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)

# @api_view(['GET','POST','PUT','DELETE'])
# def review_detail(request,pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.method == 'GET':
#         reviews = Review.objects.filter(product_id=pk)
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response (serializer.data, status=200)

#     elif request.method == 'POST':
#         request.data.update({"product": pk})
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid() == True:
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.data.product, status=400)

#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)

#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


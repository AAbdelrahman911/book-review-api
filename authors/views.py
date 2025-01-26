from django.shortcuts import get_object_or_404
from . import models
from .serializers import *
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.generics import GenericAPIView
from rest_framework.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.throttling import UserRateThrottle


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.is_author
    

class BookListCreateView(GenericAPIView):
    permission_classes = [IsAuthenticated, IsAuthor]
    filter_backends = [filters.SearchFilter]
    search_fields = ['genre', 'author__name']
    throttle_classes = [UserRateThrottle]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookInputSerializer
        return BookSerializerOutput

    def get_queryset(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(author = request.user.profile)

        return Response(
            {
                'books': BookSerializerOutput(instance).data,
                'author': ProfileOutputSerializer(instance.author).data,
            },
            status=status.HTTP_201_CREATED
        )
    
    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

class BookDetailView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return BookInputSerializer
        return BookSerializerOutput

    def get_object(self):
        return get_object_or_404(Book, pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_book = serializer.save()
        return Response(self.get_serializer(updated_book).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_book = serializer.save()
        return Response(self.get_serializer(updated_book).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorListCreateView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'bio']
    throttle_classes = [UserRateThrottle]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProfileInputSerializer
        return ProfileOutputSerializer
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)  

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            return Response(
                {"detail": "User already has a profile."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

class AuthorDetailView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProfileInputSerializer
        return ProfileOutputSerializer

    def get_object(self):
        return get_object_or_404(Profile, pk=self.kwargs['pk'], user=self.request.user)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    throttle_classes = [UserRateThrottle]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = user.profile
            return Response(
                {
                    'message': 'User Registred Successfully.',
                    'profile': ProfileOutputSerializer(profile).data
                }, status= status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request , *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username = username , password = password)
            
            if user:
                refresh = RefreshToken.for_user(user)
                profile = user.profile
                return Response(
                    {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                        'profile': ProfileOutputSerializer(profile).data
                    }, status= status.HTTP_200_OK
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProfileInputSerializer
        return ProfileOutputSerializer
    
    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = self.get_serializer(profile, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ReviewListCreateView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReviewInputSerializer
        return ReviewOutputSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_id'])

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        book_id = self.kwargs['book_id']
        book = get_object_or_404(Book, id=book_id)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book, user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ReviewDetailView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ReviewInputSerializer
        return ReviewOutputSerializer

    def get_object(self):
        return get_object_or_404(Review, pk=self.kwargs['pk'], user=self.request.user)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

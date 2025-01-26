from rest_framework import serializers
from .models import *

class ProfileOutputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'bio', 'date_of_birth', 'is_author']


class ProfileInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'date_of_birth', 'is_author','profile_picture']




class BookSerializerOutput(serializers.ModelSerializer):
    author = ProfileOutputSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'publication_date', 'genre']

class BookInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'genre']



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    bio = serializers.CharField(write_only = True, required = False)
    date_of_birth = serializers.DateField(write_only = True, required = False)
    is_author = serializers.BooleanField(write_only = True, required = False)
    email = serializers.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'date_of_birth', 'is_author']

    def create(self, validated_data):
        bio = validated_data.pop('bio', None)
        date_of_birth = validated_data.pop('date_of_birth', None)
        is_author = validated_data.pop('is_author', False)

        user = User.objects.create_user(
        username= validated_data['username'],
        password= validated_data['password'],
        email= validated_data['email']
    )
        
        Profile.objects.create(
            user = user,
            bio = bio,
            date_of_birth = date_of_birth,
            is_author = is_author
        )

        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ReviewOutputSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = Review
        fields = ['id','user','rating','comment','created_at']


class ReviewInputSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=10)
    class Meta:
        model = Review
        fields = ['rating','comment']
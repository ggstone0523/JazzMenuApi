from django.contrib.auth.models import User, Group
from .models import JazzCategory, genre, region, character, era
from rest_framework import viewsets, generics, permissions
from .serializers import UserSerializer, GroupSerializer, JazzCategorySerializer, GenreSerializer, RegionSerializer, CharacterSerializer, EraSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# JazzCategory API

class JazzCategoryList(generics.ListAPIView):
    queryset = JazzCategory.objects.all()
    serializer_class = JazzCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class JazzCategoryDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = JazzCategory.objects.all()
    serializer_class = JazzCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Genre API

class GenreList(generics.ListCreateAPIView):
    queryset = genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Region API

class RegionList(generics.ListCreateAPIView):
    queryset = region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Character API

class CharacterList(generics.ListCreateAPIView):
    queryset = character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Era API

class EraList(generics.ListCreateAPIView):
    queryset = era.objects.all()
    serializer_class = EraSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = era.objects.all()
    serializer_class = EraSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

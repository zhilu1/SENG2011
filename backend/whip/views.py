from django.shortcuts import render
from .serializers import UserSerializer, User, \
    Post, PostSerializer, \
    Parameter, ParameterSerializer, \
    Bid, BidSerializer,\
    Location, LocationSerializer,\
    Message, MessageSerializer,\
    Event, EventSerializer
from rest_framework import viewsets,permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, NotAuthenticated


# Own premission  
from .permission import GuestCreateOnly,OwnerUpdateOnly,\
    IsAdminOrReadOnly,IsOwnerOrReadOnly

class LocationViewset(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # only for test use 
    permission_classes = [OwnerUpdateOnly,]

    
    """
    Get method could only get the element of current user
    """
    def list(self, request):
        if request.user and request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        # else: not authenticated 
        # raise not authenticated
        raise NotAuthenticated()
    def retrieve(self, request, pk=None):
        return self.list(request)

    """
    Update method will only point to current user 
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        # the instance will only point to current user 
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    """ Prevent destory """
    def destroy(self):
        # not been able to destory
        return Response(status=status.HTTP_404_NOT_FOUND)

class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
    permission_classes = [IsAdminOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @action(detail= True, methods = ["POST"], url_name = "create_sub_post")
    def post(self, request, pk = None):
        # get the meta data of this event 
        event = self.get_object()


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    # only bidder bidder can change it post
    permission_classes = [IsOwnerOrReadOnly]

    @action(detail = True, methods = ['POST'], url_name='Rate-Poster')
    def rate(self, request,pk= None):
        # get the post object from the pk specified 
        bid = self.get_object()
        # use a method in object to choose the bidder 
        bid.rate(request.data["rate"])

        # wrap the serializer and with this bid detail 
        serializer = self.get_serializer(bid)

        # return back this bid detail 
        return Response(serializer.data)

    """
    Overwritten the DestroyModelMixin's function
    """
    def perform_destroy(self, instance):
        if instance.state in ["BD", "US"]:
            # only perform destory at bidding state
            # perform soft destory 
            instance.state = "CL"
            instance.save()
 

    

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    """
    TODO: need to prevent mutiple time state change
    """

    @action(detail = True, methods = ['POST'], url_name='Choose Bidder')
    def choose(self, request,pk= None):
        # get the post object from the pk specified 
        post = self.get_object()
        # use a method in object to choose the bidder 
        post.choose(request.data["id"])

        # wrap the serializer and with this post detail 
        serializer = self.get_serializer(post)

        # return back this post detail 
        return Response(serializer.data)

    @action(detail = True, methods = ['POST','GET'], url_name='Finish Post')
    def finish(self, request,pk= None):
        # get the post object from the pk specified 
        post = self.get_object()
        # use a method in object to choose the bidder 
        post.finish()

        # wrap the serializer and with this post detail 
        serializer = self.get_serializer(post)

        # return back this post detail 
        return Response(serializer.data)

    @action(detail = True, methods = ['POST'], url_name='Rate-Bidder')
    def rate(self, request,pk= None):
        # get the post object from the pk specified 
        post = self.get_object()
        # use a method in object to choose the bidder 
        post.rate(request.data["rate"])

        # wrap the serializer and with this post detail 
        serializer = self.get_serializer(post)

        # return back this post detail 
        return Response(serializer.data) 

    """
    Overwritten the DestroyModelMixin's function
    """
    def perform_destroy(self, instance):
        # perform soft destory 
        instance.state = "CL"
        instance.save()
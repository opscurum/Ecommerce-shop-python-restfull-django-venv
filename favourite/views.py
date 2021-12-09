from rest_framework import status, permissions

from .models import Favourite, FavouriteSerializer
from rest_framework import viewsets, mixins

# Create your views here.


class FavouriteViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows Favourite to be viewed or edited.
    """
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(user=user)


    #def destroy(self, *args, **kwargs):
    #    instance = self.get_object()
    #    if instance.user.id != self.request.user.id:
    #        return Response(status=status.HTTP_401_UNAUTHORIZED)
    #    self.perform_destroy(instance)
    #    return Response(status=status.HTTP_204_NO_CONTENT)


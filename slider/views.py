from rest_framework import  permissions
from .models import Slider, SliderSerializer
from rest_framework import viewsets


# Create your views here.


class SliderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows slider to be viewed or edited.
    """
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    def get_queryset(self):
        
        return Slider.objects.filter()

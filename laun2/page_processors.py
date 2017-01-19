from mezzanine.pages.page_processors import processor_for

from .models import SlideImage



@processor_for(SlideImage)

def Image(request, page):

    image = SlideImage.objects.all()

    return {'image': list(image)}

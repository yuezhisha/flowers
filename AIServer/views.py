from io import BytesIO
import os
from django.views.decorators.csrf import csrf_exempt
from .mqtt import mqtt_client
from .models import Flowers
from .CNNModel import use
from PIL import Image
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from .form import ImageUploadForm
# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def getData(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        image_file = form.cleaned_data['image']
        image = Image.open(image_file)
        # image_file_path = os.path.join('./images/', image.name)
        # with open(image_file_path,'wb') as re:
        #     for chunk in image.chunk():
        #         re.write(chunk)
        image_io = BytesIO()
        image.save(image_io, format='PNG') 
        image_io.seek(0)
        with open('./AIServer/image/ilic.png', 'wb') as f:
            f.write(image_io.getvalue())
        predict_class = use.predict('./AIServer/image/ilic.png')
        flowers=Flowers.objects.filter(flower_id=predict_class)
        try:
            for i in flowers :
                name = i.flower_name
                category=i.category
                description = i.description
            resoult = {
                'name':name,
                'category':category,
                'description':description
            }
            message = str(name + category + description)
            mqtt_client.publish('flowers/name',resoult['name'])
            mqtt_client.publish('flowers/category',resoult['category'])
            mqtt_client.publish('flowers/description',resoult['description'])
            return JsonResponse(resoult)
        except:
            resoult = {
                "error":'图片未知'
            }
            return JsonResponse(resoult)

def main(request):
    return render(request,'main.html')
def csrf(request):
    csrf = get_token(request)
    return JsonResponse({'csrftoken':csrf})
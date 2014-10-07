stdimage-serializer
===================

## Installation
1. Easy peasy, just with pip
  ```
  pip install django-stdimage-serializer
  ```
2. Add ```stdimage_serializer``` in your INSTALLED_APPS


## Usage

With the stdimage-serializer you can easily show all the variations that you have set up with your std image object. For instance when we have the following field setup in our model:

```
image = StdImageField(upload_to='images/', blank=True, 
variations={
    'large': (600, 400),
    'thumbnail': (100, 100, True),
    'medium': (300, 200),
})
```

We can easily show all the variations in a request. Just add the following code to your serializer object:
```
from stdimage_serializer.fields import StdImageField

image = StdImageField()
```

Ahh Voila! You will get the following return object in the Django Rest Framework:
```
"image": {
        "large": "https://yourdomain.com/path/to/images/image.large.png",
        "medium": "https://yourdomain.com/path/to/images/image.medium.png",
        "thumbnail": "https://yourdomain.com/path/to/images/image.thumbnail.png",
        "original": "https://yourdomain.com/path/to/images/image.png"
    }
```
__NOTE:__ original is added, this is the normal url you would receive

from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register("resident", ReidentInfoViewset)

urlpatterns = [
    
]

urlpatterns +=router.urls
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register("property", PropertyViewset)
router.register("unittype", UnitTypeViewset)
router.register("unit", UnitViewset)
router.register("unitstatus", UnitStatusViewset)

urlpatterns = [
    
]

urlpatterns +=router.urls

print('hi')
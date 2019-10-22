from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register("vendorinfo", VendorInfoViewset)
router.register("vendorinvoices", VendorInvoicesViewset)

urlpatterns = [
    
]

urlpatterns +=router.urls
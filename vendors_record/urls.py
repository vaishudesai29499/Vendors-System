# vendor_api/urls.py
from django.urls import path
from .views import (
    VendorListCreateView,
    VendorDetailView,
    PurchaseOrderListCreateView,
    PurchaseOrderDetailView,
    VendorPerformanceView,
    PurchaseOrderAcknowledgmentView,
    VendorHistoricalPerformanceView,
    vendor_list,
    delete_vendor,
    update_vendor,
    order_list,
    delete_order,
    update_order,
    index,
    contact_us
)

urlpatterns = [
    path('',index,name="hello"),
    path('contact/',contact_us),
    path('vendors/', vendor_list, name='vendor-list'),
    path('orders/', order_list, name='order-list'),
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(),
         name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(),
         name='purchase-order-detail'),
    path('vendors/<int:pk>/performance/',
         VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/',
         PurchaseOrderAcknowledgmentView.as_view(), name='purchase-order-acknowledge'),
    path('historical_performance/', VendorHistoricalPerformanceView.as_view(),
         name='vendor-historical-performance'),
    path('delete-vendor/<id>/',delete_vendor,name='delete_vendor'),
    path('delete-order/<id>/',delete_order,name='delete_order'),

    path('update-vendor/<id>/',update_vendor,name='update_vendor'),
    path('update-order/<id>/',update_order,name='update_order')
]
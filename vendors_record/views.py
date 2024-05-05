# vendor_api/views.py
from datetime import timezone
from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.shortcuts import render,redirect,HttpResponse
from .models import Vendor
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from .models import *

def index(request):
    return render(request, 'homepage.html')

def contact_us(request):
    return render(request, 'contact.html')


def vendor_list(request):
    vendors = Vendor.objects.all()
    

    if request.GET.get('search'):
        search = request.GET.get('search')
        vendors = vendors.filter(
            Q(name__icontains = search) |
            Q(contact_details__icontains = search) |
            Q(address__icontains = search) |
            Q(vendor_code__icontains = search)

            )
    
    if request.method == "POST":
      data=request.POST
      name = data.get('name')
      contact_details = data.get('contact_details')
      address = data.get('address')
      vendor_code = data.get('vendor_code')

      
    
     
      Vendor.objects.create(
        vendor_code=vendor_code,
        name=name,
        address=address,
        contact_details=contact_details
        )
         
      return redirect('/vendors/')
    
    


    return render(request, 'vendor_list.html', {'vendors': vendors})


def delete_vendor(request, id):
  queryset = Vendor.objects.get(id = id)
  queryset.delete()
  return redirect('/vendors/')

def update_vendor(request, id):
  queryset= Vendor.objects.get(id=id)
  if request.method == "POST":
      data=request.POST

      name = data.get('name')
      contact_details = data.get('contact_details')
      address = data.get('address')
      vendor_code = data.get('vendor_code')
      on_time_delivery_rate=data.get('on_time_delivery_rate')
      quality_rating_avg=data.get('quality_rating_avg')
      average_response_time=data.get('average_response_time')
      fullfillment_rate=data.get('fullfillment_rate')

      
      queryset.name=name
      queryset.contact_details=contact_details
      queryset.address=address
      queryset.vendor_code=vendor_code
      queryset.on_time_delivery_rate=on_time_delivery_rate
      queryset.quality_rating_avg=quality_rating_avg
      queryset.average_response_time=average_response_time
      queryset.fulfillment_rate=fullfillment_rate
      queryset.save()
      return redirect('/vendors/')
  context={'vendors': queryset}
  return render(request,'update_vendors.html', context)
      
def order_list(request):
     orders = PurchaseOrder.objects.all()

     if request.GET.get('search'):
        search = request.GET.get('search')
        orders = orders.filter(
            Q(po_number__icontains = search) |
            Q(items__icontains = search) |
            Q(quantity__icontains = search) |
            Q(status__icontains = search) |
            Q(quality_rating__icontains = search) |
            Q(issue_date__icontains = search) |
            Q(acknowledgement_date__icontains = search) 

            )

     if request.method == "POST":
       data = request.POST
       vendor = data.get('vendor')
       po_number = data.get('po_number')
       order_date = data.get('order_date')
       delivery_date= data.get('delivery_date')
       items = data.get('items')
       quantity = data.get('quantity')
       status = data.get('status')
       quality_rating = data.get('quality_rating')
       issue_date = data.get('issue_date')
       acknowledgement_date = data.get('acknowledgment_date')
    
 
       PurchaseOrder.objects.create (
          
           PurchaseOrder__vendor__vendor=vendor,
           po_number=po_number,
           order_date=order_date,
           delivery_date=delivery_date,
           items=items,
           quantity=quantity,
           status=status,
           quality_rating=quality_rating,
           issue_date=issue_date,
           acknowledgement_date=acknowledgement_date
           
            )
       
         
       return redirect('/orders/')

     return render(request, 'order_list.html', {'orders': orders})

def delete_order(request, id):
  queryset = PurchaseOrder.objects.get(id = id)
  queryset.delete()
  return redirect('/orders/')

def update_order(request, id):
  queryset= PurchaseOrder.objects.get(id=id)
  if request.method == "POST":
      data=request.POST

      vendor = data.get('vendor')
      po_number = data.get('po_number')
      order_date = data.get('order_date')
      delivery_date = data.get('delivery_rate')
      items=data.get('items')
      quantity=data.get('quantity')
      status=data.get('status')
      quality_rating=data.get('quality_rating')
      issue_date=data.get('issue_date')
      acknowledgement_date=data.get('acknowledgement_date')

      
      queryset.vendor=vendor
      queryset.po_number=po_number
      queryset.order_date=order_date
      queryset.delivery_date=delivery_date
      queryset.items=items
      queryset.quantity=quantity
      queryset.status=status
      queryset.quality_rating=quality_rating
      queryset.issue_date=issue_date
      queryset.acknowledgement_date=acknowledgement_date

      queryset.save()
      return redirect('/orders/')
  context={'orders': queryset}
  return render(request,'update_order.html', context)

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderAcknowledgmentView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        serializer.save(acknowledgment_date=timezone.now())


class VendorHistoricalPerformanceView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    
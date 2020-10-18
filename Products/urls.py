from django.urls import path

from Products.views import (
                        product_list_view, 
                        single_product_view, 
                        product_create_view, 
                        delete_product_view,
                        )

app_name = 'Products'
urlpatterns = [
    path('create/',product_create_view),
    path('',product_list_view, name='list_product'),
    path('<int:my_id>/',single_product_view, name='view_product'),
    path('<int:my_id>/delete/',delete_product_view, name='delete_product'),
]

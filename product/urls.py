from django.conf.urls import url
from product.views import ProductCategoryList, ProductCategoryDetail, ProductCategoryCreate, ProductCategoryUpdate, ProductCategoryDelete, UnitOfMeasurementList, UnitOfMeasurementDetail, UnitOfMeasurementCreate, UnitOfMeasurementUpdate, UnitOfMeasurementDelete, ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product-list'),
    url(r'^detail/(?P<pk>[0-9]*)/$', ProductDetail.as_view(),
        name='product-detail'),
    url(r'^add/$', ProductCreate.as_view(), name='product-add'),
    url(r'^update/(?P<pk>[0-9]*)/$', ProductUpdate.as_view(),
        name='product-update'),
    url(r'^delete/(?P<pk>[0-9]*)/$', ProductDelete.as_view(),
        name="product-delete"),

    url(r'^uom/$', UnitOfMeasurementList.as_view(),
        name='uom-list'),
    url(r'^uom/detail/(?P<pk>[0-9]*)/$', UnitOfMeasurementDetail.as_view(),
        name='uom-detail'),
    url(r'^uom/add$', UnitOfMeasurementCreate.as_view(), name='uom-add'),
    url(r'^uom/update/(?P<pk>[0-9]*)/$', UnitOfMeasurementUpdate.as_view(),
        name='uom-update'),
    url(r'uom/delete/(?P<pk>[0-9]*)/$', UnitOfMeasurementDelete.as_view(),
        name='uom-delete'),

    url(r'^category/$', ProductCategoryList.as_view(),
        name='product-category-list'),
    url(r'^category/detail/(?P<pk>[0-9]*)/$', 
        ProductCategoryDetail.as_view(),
        name='product-category-detail'),
    url(r'^category/add/$', 
        ProductCategoryCreate.as_view(), 
        name='product-category-add'),
    url(r'^category/update/(?P<pk>[0-9]*)/$',
        ProductCategoryUpdate.as_view(),
        name='product-category-update'),
    url(r'^category/delete/(?P<pk>[0-9]*)/$',
        ProductCategoryDelete.as_view(),
        name='product-category-delete'),
]

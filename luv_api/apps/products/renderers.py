from luv_api.apps.core.renderers import LuvApiJSONRendered

class ProductJSONRenderer(LuvApiJSONRendered):
    object_label = 'product'
    object_label_plural = 'products'

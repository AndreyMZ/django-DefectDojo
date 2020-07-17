from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

from dojo.models import Product, authorize_products_in_qs

User = get_user_model()


def authorize_product_or_403(user: User, product: Product) -> None:
    """
    :raises PermissionDenied:
    """
    if not is_authorized_product(user, product):
        raise PermissionDenied()


def is_authorized_product(user: User, product: Product) -> bool:
    if user.is_staff:
        return True
    else:
        single_product_qs = Product.objects.filter(pk=product.pk)
        return authorize_products_in_qs(user, single_product_qs).exists()

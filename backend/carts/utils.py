from django.core.cache import cache


def get_buyer_cart_cache(buyer_id):
    key = f"buyer_{buyer_id}_cart_list"
    data = cache.get(key)

    return data


def set_buyer_cart_cache(buyer_id, data):
    key = f"buyer_{buyer_id}_cart_list"
    cache.set(key, data, 60 * 60)


def delete_buyer_cart_cache(buyer_id):
    key = f"buyer_{buyer_id}_cart_list"
    cache.delete(key)

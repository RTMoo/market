from django.core.cache import cache


def delete_cart_cache(user_id: int):
    cache_key = f"user_{user_id}_cart_list"
    cache.delete(cache_key)

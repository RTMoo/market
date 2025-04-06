from django.core.cache import cache


def clear_review_cache(product_id: int):
    cache_key = f"product_{product_id}_reviews"

    cache.delete(cache_key)

from django.core.cache import cache
from urllib.parse import urlencode


def clear_product_cache(seller_id: int):
    # Удалить весь кэш из пагинаторов
    cache.delete_pattern("paginator*")

    # Удалить кэш списка продуктов текущего продавца
    cache.delete(f"product_list_seller_{seller_id}")


def normalize_query_dict(query_dict, allowed_fields=None):
    """
    Возвращает отфильтрованный и отсортированный словарь и строку для кэша.
    """
    if allowed_fields is not None:
        allowed_fields = set(f.lower() for f in allowed_fields)

    filtered = {}

    for key in query_dict.keys():
        if allowed_fields is None or key.lower() in allowed_fields:
            values = query_dict.getlist(key)
            filtered[key] = sorted(values)

    # строка для кэша
    encoded_query_hash = urlencode(sorted(filtered.items()), doseq=True)

    return filtered, encoded_query_hash

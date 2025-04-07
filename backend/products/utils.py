from django.core.cache import cache
from urllib.parse import urlencode


def clear_product_cache(seller_id: int):
    # Удалить весь кэш из пагинаторов
    cache.delete_pattern("paginator_page_*")

    # Удалить кэш списка продуктов текущего продавца
    cache.delete(f"product_list_seller_{seller_id}")


def normalize_query_dict(query_dict, allowed_fields=None):
    """
    Фильтрует, сортирует и возвращает стабильную строку для кэш-ключа.
    Поддерживает множественные значения.
    """
    if allowed_fields is not None:
        allowed_fields = set(f.lower() for f in allowed_fields)

    filtered = {}

    for key in query_dict.keys():
        if allowed_fields is None or key.lower() in allowed_fields:
            values = query_dict.getlist(key)
            filtered[key] = sorted(values)  # сортировка значений, если их несколько

    # сортировка ключей и построение строки
    sorted_items = sorted(filtered.items())
    return urlencode(sorted_items, doseq=True)

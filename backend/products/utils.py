from django.core.cache import cache


def clear_product_cache(seller_id: int):
    # Удалить весь кэш из пагинаторов
    cache.delete_pattern("paginator_page_*")

    # Удалить кэш списка продуктов текущего продавца
    cache.delete(f"product_list_seller_{seller_id}")

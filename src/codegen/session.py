import requests_cache

# avoid circular import
session = requests_cache.CachedSession("carastix_cache")

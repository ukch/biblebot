import os
import redis as _redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = _redis.from_url(redis_url)

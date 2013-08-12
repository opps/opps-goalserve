# coding: utf-8

import celery
from .crawler import Crawler

GID = 'c93ce5a5b570433b8a7d96b3c53f119d'

@celery.task
def get_matches(country_name, match_id=None):
    crawler = Crawler(GID)
    crawler.get_matches(countries=[country_name], match_id=match_id, get_players=False)

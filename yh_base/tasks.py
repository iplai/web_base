from celery.task import task

from dynamic_scraper.utils.task_utils import TaskUtils
from yh_base.models import Website, Article


@task()
def run_spiders():
    t = TaskUtils()
    t.run_spiders(Website, 'scraper', 'scraper_runtime', 'article_spider')


@task()
def run_checkers():
    t = TaskUtils()
    t.run_checkers(Article, 'news_website__scraper', 'checker_runtime', 'article_checker')

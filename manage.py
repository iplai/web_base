#!/usr/bin/env python
from __future__ import unicode_literals
import os
import sys

if __name__ == "__main__":
    # import web_base.settings
    # import yh_base.scraper.settings
    # print web_base.settings.PROJECT_ROOT
    # print yh_base.scraper.settings.PROJECT_ROOT
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_base.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

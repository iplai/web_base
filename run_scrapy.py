# coding=utf-8
from scrapy import cmdline

command = 'scrapy crawl article_spider -a id=1 -a do_action=yes'
# command = 'scrapy crawl --output=output.json --output-format=json article_spider -a id=1'
cmdline.execute(command.split())

# scrapy crawl [--output=FILE --output-format=FORMAT] spider_name -a id=REF_OBJECT_ID
#  [-a do_action=(yes|no)] 当指定输出文件时，不要本参数
#  [-a run_type=(TASK|SHELL)]
#  [-a max_items_read={Int}]
#  [-a max_items_save={Int}]
#  [-a max_pages_read={Int}]
#  [-a output_num_mp_response_bodies={Int}]
#  [-a output_num_dp_response_bodies={Int}]

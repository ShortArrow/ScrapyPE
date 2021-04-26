from scrapy.cmdline import execute
import sys

args = sys.argv

execute(['scrapy','crawl', args[1]])
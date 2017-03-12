# coding:utf-8
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_base.settings")
'''
Django 版本大于等于1.7的时候，需要加上下面两句
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
import django

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from yh_base.models import Account
    f = open('accounts.txt')
    f.readline()  # 不要首行header
    for line in f:
        line = line[1:-1]  # 去掉头部|和尾部换行符
        if line.endswith('|'):
            line = line[:-1]  # 去掉尾部|
        args = line.split('|')
        # 避免重复导入数据
        # Account.objects.get_or_create()
        Account.objects.get_or_create(title=args[1], username=args[2], password=args[3], remarks=args[4], tag=args[5], url=args[6])
    f.close()


if __name__ == "__main__":
    main()
    print('Done!')

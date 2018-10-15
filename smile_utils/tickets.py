#! /usr/bin/python
# coding:utf-8

""" 命令行火车票查询器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help 显示帮助菜单
    -g        高铁
    -d        动车
    -t        特快
    -k        快速
    -z        直达

Example:
    tickets 北京 上海 2016-12-28
    tickets -dg 杭州 天水 2016-12-24
"""
import requests
try:
    import cPickle as pickle
except ImportError:
    import pickle
from prettytable import PrettyTable
from docopt import docopt
from stations import stations

class TrainsCollections:
    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

    def __init__(self, available_trains, options):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self, raw_train):
        duration = raw_train.get('lishi').replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for raw_train in self.available_trains:
            train_no = raw_train['station_train_code']
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                    train_no,
                    '\n'.join([raw_train['from_station_name'],
                               raw_train['to_station_name']]),
                    '\n'.join([raw_train['start_time'],
                               raw_train['arrive_time']]),
                    self._get_duration(raw_train),
                    raw_train['zy_num'],
                    raw_train['ze_num'],
                    raw_train['rw_num'],
                    raw_train['yw_num'],
                    raw_train['yz_num'],
                    raw_train['wz_num'],
                ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    from_station=stations.get(arguments['<from>'])
    to_station=stations.get(arguments['<to>'])
    date=arguments['<date>']

    #构建url
    url='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'\
        .format(date,from_station,to_station)

    options=''.join([
        key for key,value
            in arguments.items()
        if value is True
    ])

    r =requests.get(url,verify=False)
    available_trains = r.json()['data']['datas']
    TrainsCollections(available_trains,options).pretty_print()


if __name__ == '__main__':
    cli()

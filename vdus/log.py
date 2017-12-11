#!/bin/env python
# coding:utf-8

import logging

logger = logging.getLogger('vduslogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('vdus.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

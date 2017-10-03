# -*- coding: utf-8 -*-
# Copyright (c) 2017-2020 Rhilip <rhilipruan@gmail.com>
# Licensed under the GNU General Public License v3.0

import re
import time

TABLE_INFO_LIST = "info_list"
TABLE_SEED_LIST = "seed_list"

Video_Containers = [
    # From: https://mediaarea.net/en/MediaInfo/Support/Formats
    ".mkv",  # Matroska
    ".mp4",  # Mpeg 4 container
]

REV_TAG = [
    "repack", "proper", "real",  # Series
    "v2", "rev"  # Anime
]

pat_rev_tag = re.compile("|".join(REV_TAG))


def period_f(func, sleep_time):
    while True:
        func()
        time.sleep(sleep_time)

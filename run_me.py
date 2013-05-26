#!/usr/bin/env python
from exfm import ExfmDownloader
exfm = ExfmDownloader()
username = raw_input("Enter exfm username: ")
print "\rnice stash :) now go make a cup of tea while this gets downloaded..\r"
exfm.get_user_loved(username)

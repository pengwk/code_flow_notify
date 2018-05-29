#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

def notify(title, text):
  os.system("""
            osascript -e 'display notification "{}" with title "{}"'
            """.format(text, title))

def code_flow_check(ui, repo, hooktype, **kwargs):
  notify("检查代码风格和运行单元测试", "别忘了，很重要！")
  return False

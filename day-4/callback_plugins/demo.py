from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
import sys
import json

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

class CallbackModule(CallbackBase):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'demo'

    def show(self, task, host, result, caption):
        buf = "<<< {0} | {1} | {2} | rc={3} >>>\n".format(task, host, caption,
                                                     result.get('rc', 'n/a'))
        buf1 = ""
        buf += result.get('stdout', '')
        if not "% Total" in result.get('stderr', ''):
            buf += result.get('stderr', '')
        if not type(result.get('msg', '')) == type(dict()):
            buf += result.get('msg', '')
        else:
            buf1 = result.get('msg', '')
        print((buf + "\n"), buf1)

    def v2_runner_on_failed(self, result, ignore_errors=False):
        sys.stdout.write(RED)
        self.show(result._task, result._host.get_name(), result._result, "FAILED")
        sys.stdout.write(RESET)

    def v2_playbook_on_notify(self, result, handler):
        host = result._host.get_name()
        sys.stdout.write(CYAN)
        self.show(result._host.get_name(), handler)
        sys.stdout.write(RESET)

    def v2_playbook_on_handler_task_start(self, task):
        pass

    def v2_runner_on_ok(self, result):
        sys.stdout.write(GREEN)
        self.show(result._task, result._host.get_name(), result._result, "OK")
        sys.stdout.write(RESET)

    def v2_runner_on_skipped(self, result):
        sys.stdout.write(BLUE)
        self.show(result._task, result._host.get_name(), result._result, "SKIPPED")
        sys.stdout.write(RESET)

    def v2_runner_on_unreachable(self, result):
        sys.stdout.write(BLUE)
        self.show(result._task, result._host.get_name(), result._result, "UNREACHABLE")
        sys.stdout.write(RESET)

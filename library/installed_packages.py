#!/usr/bin/python
from ansible.module_utils.basic import *
import subprocess

def exec_command(cmd):
    result = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        shell=True
    ).stdout.readlines()
    return [x.rstrip() for x in result]

def main():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    stdout = exec_command("dpkg-query -f '${binary:Package}\n' -W")
    module.exit_json(
        packages=stdout, changed=False
    )

if __name__ == '__main__':
    main()

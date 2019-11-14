#!/usr/bin/env python3

def exec_command(cmd):
    result = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        shell = True
    ).stdout.readlines()
    return [x.rstrip() for x in result]

def main():
    stdout = exec_command("dpkg-query -f '${binary:Package}\n' -W")
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    module.exit_json(
        packages = stdout,
    )

from ansible.module_utils.basic import AnsibleModule
import subprocess

if __name__ == '__main__':
    main()

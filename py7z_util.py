import os
import platform
import subprocess
from datetime import datetime


def get7zlib():
    lib_dir = os.path.dirname(__file__)
    return lib_dir


def print_output(output):
    for f in output.stdout:
        try:
            if isinstance(f, bytes):
                if f.decode().strip() != "":
                    print(datetime.now(), f.decode().rstrip())
            else:
                print(f)
        except UnicodeDecodeError as e:
            print(e.__traceback__)


def execute_7z_command(compress_cmd):
    os_platform=platform.system()
    if os_platform == "Windows":
        result = subprocess.check_output("7z", shell=True)
        if "Igor Pavlov" in result.decode():
            os.system(compress_cmd)
        else:
            output = subprocess.Popen(compress_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=get7zlib(), shell=True)
            print_output(output)
    if os_platform == "Linux":
        os.system(compress_cmd)


def compress(file_7z, dirs, excludes=None, additions=None):
    print(type(dirs))
    compress_cmd = '7z a "{}" "{}"'.format(file_7z, dirs)
    if not isinstance(dirs, str):
        compress_cmd = '7z a "{}" {}'.format(file_7z, " ".join(['"{}"'.format(i) for i in dirs]))
    if excludes:
        exs = "".join([" -xr!" + i for i in excludes])
        compress_cmd += exs
    if additions:
        if not additions.startswith(r" "):
            additions = " " + additions
        compress_cmd += additions
    # add log
    compress_cmd += " -bb3"
    print(compress_cmd)
    execute_7z_command(compress_cmd)


def decompress(file_7z, decompress_dir, excludes=None, additions=None):
    decompress_cmd = '7z x "{}" -o"{}"'.format(file_7z, decompress_dir)
    if excludes:
        exs = "".join([" -xr!" + i for i in excludes])
        decompress_cmd += exs
    if additions:
        if not additions.startswith(r" "):
            additions = " " + additions
        decompress_cmd += additions
    # add log
    decompress_cmd += " -bb3"
    print(decompress_cmd)
    execute_7z_command(decompress_cmd)



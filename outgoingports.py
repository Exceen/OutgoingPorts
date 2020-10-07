import os
from multiprocessing import Process
import subprocess
import time


def main():
    port_start = 1
    port_end = 443
    port_end = 9999


    processes = []
    for port in range(port_start, port_end+1):
        process = Process(target=test_port, args=(port, ))
        process.start()
        processes.append(process)

    # while len(processes) > 0:
    #     print('\t' + str(len(processes)), end="\r")
    #     for process in processes:
    #         if not process.is_alive():
    #             processes.remove(process)

def test_port(port):
    proc = subprocess.Popen(["c:/windows/system32/curl.exe", "-s", "portquiz.net:" + str(port)], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.decode("utf-8")
    
    if 'successful' in out:
        print (':' + str(port) + (' ')*20)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)



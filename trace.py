import os


def traceroute(destination):
    command = 'traceroute -q ' + destination
    results = os.popen(command).read()
    return(results)


if __name__ == '__main__':
    results = traceroute('8.8.8.8')
    print(results)

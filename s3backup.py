import boto, sys

check_args(argv):
    try:
        args, opts = getopt.getopt(argv, "b:f:", ["bucket", "file"])

if __name__ == '__main__':
    check_args(sys.argv[1:])

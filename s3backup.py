import boto, sys, getopt, os.path

def check_file(backup_file):
    if not os.path.isfile(backup_file):
        print "To backup file doesn't exist"
        sys.exit(2)

def check_args(argv):
    usage = "Usage: s3backup.py -b <bucket name> -f <file to backup"
    try:
        opts, args = getopt.getopt(argv, "b:f:")
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    return opts

if __name__ == '__main__':
    args = check_args(sys.argv[1:])

    check_file(args[1][1])

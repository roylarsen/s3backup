import boto, sys, getopt, os.path

def connect_s3():
   s3 = boto.connect_s3()
   return s3

def check_file(backup_file):
    if not os.path.isfile(backup_file):
        print "To backup file doesn't exist"
        sys.exit(2)

def check_bucket(conn, bucket):
    test = conn.lookup(bucket, validate=True)
    if test is None:
        print "Bucket does not exist"
        sys.exit(2)
	
def get_bucket(conn, bucket):
    bucket_obj = conn.get_bucket(bucket)
    return bucket_obj

def add_file(s3, bucket, to_backup):
    key = bucket.get_key(to_backup)

    if key.exists is None:
        key = bucket.new_key(to_backup)
        key.set_contents_from_filename(to_backup)
        key.set_acl('public-read')

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
    conn = connect_s3()
    check_file(args[1][1])
    check_bucket(conn, args[0][1])
    bucket = get_bucket(conn, args[0][1])

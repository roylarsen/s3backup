import boto, sys, getopt, os.path

#sets up s3 connection
def connect_s3():
   s3 = boto.connect_s3()
   return s3

#Checks for existence of file to backup
def check_file(backup_file):
    if not os.path.isfile(backup_file):
        print "To backup file doesn't exist"
        sys.exit(2)

#Checks existence of s3 bucket to backup to
#TODO: Add support for creating a bucket
def check_bucket(conn, bucket):
    test = conn.lookup(bucket, validate=True)
    if test is None:
        print "Bucket does not exist"
        sys.exit(2)

#Gets s3 bucket object
def get_bucket(conn, bucket):
    bucket_obj = conn.get_bucket(bucket)
    return bucket_obj

#uploads named file to s3 bucket and sets permissions
def add_file(s3, bucket, to_backup):
    key = bucket.get_key(to_backup)

    if key.exists is None:
        key = bucket.new_key(to_backup)
        key.set_contents_from_filename(to_backup)
        key.set_acl('public-read')

#Verifies you're using the script correctly
def check_args(argv):
    usage = "Usage: s3backup.py -b <bucket name> -f <file to backup"
    try:
        opts, args = getopt.getopt(argv, "b:f:")
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    return opts

#Main flow control
if __name__ == '__main__':
    args = check_args(sys.argv[1:])
    conn = connect_s3()
    check_file(args[1][1])
    check_bucket(conn, args[0][1])
    bucket = get_bucket(conn, args[0][1])

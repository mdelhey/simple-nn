def getMyData(dir_out='data/', config_file='config.yaml'):
    '''
    Grabs my data.mat file from the web.
    '''
    import yaml, subprocess, os

    # Check to see if file exists
    if (os.path.isfile(dir_out + 'data.mat')):
        ans = raw_input('data.mat exists, overwrite? (y/n)')
        if (ans == 'y') or (ans == 'Y'):
            print 'Ok. Overwriting data.mat'
        else:
            print 'Not overwritting file. Stopping'
            return 1

    # Get url from config file
    config = yaml.load(open(config_file))
    url = config['data_url']

    # Use wget to grab data
    cmd = 'wget -P ' + dir_out + ' ' + url
    subprocess.call(cmd, shell=True)

    return 0

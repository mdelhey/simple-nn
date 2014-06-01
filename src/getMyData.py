def getMyData(config_file='../config.yaml', dir_out='data/', verbose=True):
    '''
    Grabs my data.mat file from Dropbox. Puts it in the right folder.
    Assumes that we are in home dir. Grabs url from config file.
    '''
    import yaml, subprocess, os

    # Check to see if file exists
    if os.path.isfile(dir_out + 'data.mat') and verbose:
        ans = raw_input('data.mat exists, overwrite? (y/n)')
        if (ans == 'y') or (ans == 'Y'):
            print 'Ok. Overwriting data.mat'
        else:
            print 'Not overwritting file. Stopping'
            return 
    
    # Get url from config file
    config = yaml.load(open(config_file))
    url = config['data_url']

    # Use wget to grab data
    cmd = 'wget -P ' + dir_out + ' ' + url
    subprocess.call(cmd, shell=True)

    return 

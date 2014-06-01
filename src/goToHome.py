def goToHome(config_file='../config.yaml'):
    '''
    Go to home project directory. 
    '''
    import yaml, os

    config = yaml.load(open(config_file))
    home_dir = config['home_dir']

    os.chdir(home_dir)
    
    return

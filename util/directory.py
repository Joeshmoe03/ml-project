import os
from util.dataset import ASLBatchLoader, ASLDataPaths, split_data, save_data, load_saved_data

def initializeDir(dir: str):
    '''
    Initialize a directory if it does not exist.
    
    Parameters:
        dir: str - The directory to initialize.
        
        Returns:
            bool - True if the directory was created, False if it already existed.
    '''
    if not os.path.exists(dir):
        os.makedirs(dir)
        return True
    return False
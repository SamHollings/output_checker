""""Contains functions which will scan a directory and apply the battery of checks"""
import glob
import pandas


def get_all_filepaths_in_directory(dir_path):
  """Returns a list of all the filepaths in the directory"""
  all_files = glob.glob(dir_path + '/**/*', recursive=True)
  return all_files


def scan_directory(dir_path, checks=[]):
  """Applies the supplied checks to each file in the directory"""

  list_file_paths = get_all_filepaths_in_directory(dir_path)

  df_files = pd.DataFrame(dict(path=list_file_paths)
  return  
  
  

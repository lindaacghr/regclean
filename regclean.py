import os
import winreg
import logging

# Set up logging configuration
logging.basicConfig(filename='regclean.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def delete_registry_key(hive, path, key):
    """Delete a registry key."""
    try:
        with winreg.OpenKey(hive, path, 0, winreg.KEY_ALL_ACCESS) as open_key:
            winreg.DeleteKey(open_key, key)
        logging.info(f"Deleted registry key: {path}\\{key}")
    except FileNotFoundError:
        logging.warning(f"Registry key not found: {path}\\{key}")
    except PermissionError:
        logging.error(f"Permission denied while deleting key: {path}\\{key}")
    except Exception as e:
        logging.error(f"Error deleting key {path}\\{key}: {str(e)}")

def clean_unused_registry_entries():
    """Clean unused and old registry entries to boost system performance."""
    # Example paths to clean, add more as needed
    registry_paths = [
        (winreg.HKEY_CURRENT_USER, r"Software\OldApplication"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Unused"),
    ]

    for hive, path in registry_paths:
        try:
            with winreg.OpenKey(hive, path) as key:
                num_subkeys, num_values, last_modified = winreg.QueryInfoKey(key)
                if num_subkeys == 0 and num_values == 0:
                    delete_registry_key(hive, path.rsplit("\\", 1)[0], path.split("\\")[-1])
        except FileNotFoundError:
            logging.warning(f"Registry path not found: {path}")
        except PermissionError:
            logging.error(f"Permission denied while accessing path: {path}")
        except Exception as e:
            logging.error(f"Error accessing registry path {path}: {str(e)}")

if __name__ == "__main__":
    if os.name == 'nt':
        logging.info("Starting RegClean to clean the Windows registry.")
        clean_unused_registry_entries()
        logging.info("Registry cleaning completed.")
    else:
        logging.error("RegClean is designed for Windows systems only.")
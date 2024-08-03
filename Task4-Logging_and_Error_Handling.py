import logging
import os
import shutil
import datetime

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bulk_pst.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def create_backup(source_dirs, backup_location):
    logger.info("Starting backup process")
    try:
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_dir = os.path.join(backup_location, f"backup_{timestamp}")
        os.makedirs(backup_dir, exist_ok=True)
        logger.info(f"Created backup directory at {backup_dir}")
        
        for source_dir in source_dirs:
            if os.path.exists(source_dir):
                dest_dir = os.path.join(backup_dir, os.path.basename(source_dir))
                shutil.copytree(source_dir, dest_dir)
                logger.info(f"Backed up {source_dir} to {dest_dir}")
            else:
                logger.warning(f"Source directory {source_dir} does not exist.")
        
        logger.info("Backup completed successfully.")
    except Exception as e:
        logger.error("An error occurred during the backup process", exc_info=True)

def restore_backup(backup_dir, restore_dirs):
    logger.info("Starting restore process")
    try:
        if not os.path.exists(backup_dir):
            logger.error(f"Backup directory {backup_dir} does not exist.")
            return
        
        for restore_dir in restore_dirs:
            backup_source = os.path.join(backup_dir, os.path.basename(restore_dir).replace('_restored', ''))
            if os.path.exists(backup_source):
                shutil.copytree(backup_source, restore_dir, dirs_exist_ok=True)
                logger.info(f"Restored {restore_dir} from {backup_source}")
            else:
                logger.warning(f"Backup source {backup_source} does not exist.")
        
        logger.info("Restore completed successfully.")
    except Exception as e:
        logger.error("An error occurred during the restore process", exc_info=True)

if __name__ == "__main__":
    source_dirs = ["C://Users//Lenovo//Desktop//source1", "C://Users//Lenovo//Desktop//source2"]
    backup_location = "C://Users//Lenovo//Desktop//backup"

    create_backup(source_dirs, backup_location)

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_dir = os.path.join(backup_location, f"backup_{timestamp}")

    restore_dirs = [
        "C://Users//Lenovo//Desktop//source1",
        "C://Users//Lenovo//Desktop//source2"
    ]
    restore_backup(backup_dir, restore_dirs)

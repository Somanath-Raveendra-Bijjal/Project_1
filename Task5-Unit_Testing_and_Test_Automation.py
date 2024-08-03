
import os
import shutil
import datetime

def create_backup(source_dirs, backup_location):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_dir = os.path.join(backup_location, f"backup_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    
    for source_dir in source_dirs:
        if os.path.exists(source_dir):
            dest_dir = os.path.join(backup_dir, os.path.basename(source_dir))
            shutil.copytree(source_dir, dest_dir)
        else:
            raise FileNotFoundError(f"Source directory {source_dir} does not exist.")
    
    return backup_dir


import os
import shutil
import unittest
from bulk_pst import create_backup

class TestBulkPst(unittest.TestCase):
    def setUp(self):
        self.source_dir = "test_source"
        self.backup_dir = "test_backup"
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.backup_dir, exist_ok=True)
        with open(os.path.join(self.source_dir, "test_file.txt"), 'w') as f:
            f.write("This is a test file.")

    def tearDown(self):
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.backup_dir)

    def test_create_backup(self):
        source_dirs = [self.source_dir]
        backup_dir_path = create_backup(source_dirs, self.backup_dir)
        
        self.assertTrue(os.path.exists(backup_dir_path))
        backed_up_file = os.path.join(backup_dir_path, "test_source", "test_file.txt")
        self.assertTrue(os.path.exists(backed_up_file))
        with open(backed_up_file, 'r') as f:
            content = f.read()
            self.assertEqual(content, "This is a test file.")

    def test_create_backup_nonexistent_directory(self):
        source_dirs = ["nonexistent_directory"]
        with self.assertRaises(FileNotFoundError):
            create_backup(source_dirs, self.backup_dir)

if __name__ == '__main__':
    unittest.main()

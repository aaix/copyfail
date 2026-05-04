import os
import stat

print(f"{'permissions':<12} {'owner':<8} {'path'}")
print()
for root, dirs, files in os.walk("/"):
    for name in files:
        file_path = os.path.join(root, name)
        try:
            info = os.stat(file_path)
            if info.st_uid == 0:
                if info.st_mode & stat.S_ISUID:
                    mode_str = stat.filemode(info.st_mode)
                    print(f"{mode_str:<12} root     {file_path}")
        
        except (PermissionError, FileNotFoundError):
            continue

'''
'''

import os

def atomic_write(filename, contents, mode="wb"):
    backup = BackupedFiles([filename], ".temp")
    backup.create()
    backup_filename = backup.of(filename)

    with open(backup_filename, mode) as dst:
        dst.write(contents)

    fns = (backup_filename, filename)
    print("Moving '%s' to '%s' atomically" % fns)
    try:
        os.rename(*fns)
    except Exception:
        backup.remove()
        print("Error on moving file '%s'" % fns)
        raise

def parse_varfile(txt):
    cfg = {}
    for line in txt.split("\n"):
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        try:
            key, value = line.split("=", 1)
            cfg[key] = value.strip("\"' \n")
        except:
            pass
    return cfg

def truncate(filename):
    """Truncate the given file to the length 0
    """
    with open(filename, "wb"):
        pass

def get_contents(src):
    with open(src, "r") as f:
        contents = f.read()
    return contents

class File(object):
    filename = None

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Read the contents of a file
        """
        return get_contents(self.filename)

    def write(self, contents, mode="wb"):
        """Write the contents of a file
        """
        try:
            atomic_write(self.filename, contents, mode)
        except:
            with open(self.filename, mode) as dst:
                dst.write(contents)

    def touch(self):
        """Touch a file
        """
        return truncate(self.filename)

    def exists(self):
        """Determin if a file exists
        """
        return os.path.exists(self.filename)

    def delete(self):
        """Delete a file
        """
        return os.unlink(self.filename)

    def access(self, mode):
        """Check if the file can be accessed
        """
        return os.access(self.filename, mode)

class ShellVarFile(object):
    filename = None
    _fileobj = None
    create = False

    def __init__(self, filename, create=False):
        self.filename = filename
        self.create = create
        if File in type(filename).mro():
            self._fileobj = filename
        else:
            self._fileobj = File(self.filename)
            if not create and not self._fileobj.exists():
                    raise RuntimeError("File does not exist: %s" %
                                       self.filename)
            if create and not self._fileobj.exists():
                self._fileobj.touch()

    def _read_contents(self):
        return self._fileobj.read()

    def _write_contents(self, data):
        self._fileobj.write(data)

    def exists(self):
        """Return true if this file exists
        """
        return self._fileobj.exists()

    def get_dict(self):
        """Returns a dict of (key, value) pairs
        """
        data = self._read_contents()
        return parse_varfile(data)

    def write(self, cfg, remove_empty=True):
        """Write a dictinory as a key-val file
        """
        for key, value in cfg.items():
            if remove_empty and value is None:
                del cfg[key]
            if value is not None and type(value) not in [str, unicode]:
                raise TypeError("The type (%s) of %s is not allowed" %
                                (type(value), key))
        lines = []
        # Sort the dict, looks nicer
        for key in sorted(cfg.iterkeys()):
            lines.append("%s=\"%s\"" % (key, cfg[key]))
        contents = "\n".join(lines) + "\n"
        self._write_contents(contents)

    def update(self, new_dict, remove_empty):
        cfg = self.get_dict()
        cfg.update(new_dict)
        self.write(cfg, remove_empty)


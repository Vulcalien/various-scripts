# Various Scripts

A selection of scripts I wrote for myself that might also be useful to
someone else. These scripts are made for Unix-like operating systems.

### backup-repos.py
<code>./backup-repos.py</code>

Downloads all public repositories from a GitHub account to create a
backup of them. To specify which account to create a backup of, change
the line that says `USER = ''`.

By default, forks are not downloaded. If that's not desired, delete
these lines:

```python
if repo['fork']:
    print('Fork: skipping')
    continue
```

### md5sum-recursive
<code>./md5sum-recursive *path*...</code>

Like `md5sum`, but it recursively prints the MD5 hashes of directory
contents.

For example, running `./md5sum-recursive .` prints the MD5 hashes of all
files in the current directory and its subdirectories. It can be used to
easily create a checksum file. For example,
`./md5sum-recursive . > checksums.md5` will create a checksum file,
which can then be checked with `md5sum --check checksums.md5`.

### battery
<code>./battery</code>

Prints the charge percentage of the device (provided it has one, of
course).

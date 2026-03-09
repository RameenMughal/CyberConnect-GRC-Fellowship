# DISKO 1 💿

Platform: [PicoCTF](https://play.picoctf.org)

Challenge: [DISKO 1](https://play.picoctf.org/practice/challenge/505?page=1&search=DISK)

## Description

Can you find the flag in this disk image?

## Concept

A disk image is a complete copy of a storage device saved into a single file. It contains everything on the disk exactly as it exists, including files, deleted data, file system structure, and metadata.

A disk image = snapshot of an entire disk stored as a file.

It copies the disk bit-by-bit, not just the visible files.

### Why Disk Images are Used in Cybersecurity / Forensics

In digital forensics and CTF challenges, disk images are used because they allow investigators to:
- Analyze deleted files
- Recover hidden data
- Inspect file system artifacts
- Maintain evidence integrity

Investigators never analyze the original disk. They analyze the image copy.

## Solution

By downloading the disk image we can check the contents of the file by `nano disko-1.dd` command. It has so many unreadable context.

<img width="840" height="322" alt="image" src="https://github.com/user-attachments/assets/cab4b5ab-cc5b-4181-ad11-d2f72d26a88a" />

First we can use the `strings disko-1.dd` command to extract meaningful characters and words from the file but it gives us many strings which is unfeasible to see the flag.

We know that the flag format is `picoCTF{}` so we can use the `strings` and `grep` command to get the flag directly.

By command `strings disko-1.dd | grep -o 'picoCTF{[^}]*}'` we get the flag!

<img width="469" height="55" alt="image" src="https://github.com/user-attachments/assets/66c3ff9e-298d-4f9f-a93a-86ce138a9b08" />



# pp-krypto

  
**Installation:**
`python3.8 -m venv venv`
`source venv/bin/activate`
`pip3 install -r requirements.txt`

  

**Run script:**
`python3.8 main.py`

**Available flags:**
`-debug` - debug, print result
`-f <filename>` - process input instead of generating new one
`-o <filename>` - save output bits to file
`-l <number>` - generate a string of set length
`-s <number>` - set custom seed
`-d` - decrypt message, requires -f and -s flags

**Generate BBS of n size:**
`python3.8 main.py --debug -l n`

Generate BBS of n size and save output to file:
`python3.8 main.py --debug -l n -o output.txt`

Encrypt a message:
`python3.8 main.py -m "Some fancy message"`
and save to file:
`python3.8 main.py -m "Some fancy message"-o output.txt`

  

Decrypt a message:
`python3.8 main.py -d -f path/to/file.txt -s <seed>`
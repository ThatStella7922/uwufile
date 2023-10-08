# uwufile
uwuify your files.

## Introduction
**uwufile** is a simple uwuifier for text files built on [uwuipy](https://github.com/Cuprum77/uwuipy). It's essentially just a wrapper around the uwuipy library, designed to make usage of it at the command line significantly easier by providing a familiar command-line driven interface, validation, error checking and nice output to let you know what's happening.

## Usage
Using **uwufile** is very simple. See the below output of uwufile.py when run with no arguments, or with the `-h`/`--help` arguments:

```
uwufile.py v1.0 - uwuify your files
ThatStella7922 (https://thatstel.la)

Help for uwufile.py v1.0:
Usage: uwufile.py input_file output_file

    input_file: The source file to uwuify
    output_file: The destination for the uwuified version
    
    Example: uwufile.py input.txt output.txt
    
    Notes: 
    - If the output file already exists, it will be overwritten
    - If the input file is a character device (such as /dev/urandom),
      it wont't be read for safety reasons
```

It takes a source file, reads the contents of the file, uwuifies it, then writes it out to a destination file.

## Requirements and Compatibility
Requires Python 3.10 or newer, and should run on any OS that runs Python 3.10.


## Credits
Includes [Cuprum77's **uwuipy**](https://github.com/Cuprum77/uwuipy) project nearly verbatim, I thank them for choosing such a permissive license. To be compliant with the license, this project is also licensed under [MIT](LICENSE).
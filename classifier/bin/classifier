#!/usr/bin/env python
import click
import os
import sys

"""
A list of known formats here can be added.

All format lists were taken from wikipedia, not all of them were added
due to extensions not being exclusive to one format such as webm, or
raw:

- Audio - https://en.wikipedia.org/wiki/Audio_file_format
- Documents - https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions
              Majority of it is from MS Office
- Images - https://en.wikipedia.org/wiki/Image_file_formats
- Video - https://en.wikipedia.org/wiki/Video_file_format

"""

DEFAULT_RULES = {
    'Archives': [
        '.7z',
        '.bz2',
        '.gz',
        '.rar',
        '.tar',
        '.tar.bz2',
        '.tar.gz',
        '.zip',
    ],
    'Documents': [
        '.doc',
        '.docx',
        '.odp',
        '.ods',
        '.odt',
        '.pdf',
        '.ppsx',
        '.ppt',
        '.pptx',
        '.xls',
        '.xlsv',
        '.xlsx',
    ],
    'Music': [
        '.aac',
        '.aiff',
        '.flac',
        '.m4a',
        '.mp3',
        '.ogg',
        '.wma',
    ],
    'Pictures': [
        '.bmp',
        '.gif',
        '.jpeg',
        '.jpg',
        '.png',
        '.svg',
        '.webp',
    ],
    'Videos': [
        '.3gp',
        '.avi',
        '.flv',
        '.mov',
        '.mp4',
        '.mpeg',
        '.mpg',
        '.ogv',
    ],
}


def flatten_rules(default_rules):
    rules = {}
    for folder in default_rules:
        for extension in default_rules[folder]:
            rules[extension] = folder
    return rules


def moveto(filename, source_folder, target_folder):
    os.rename(
        os.path.join(source_folder, filename),
        os.path.join(target_folder, filename)
    )


@click.command()
@click.option('-v', '--verbose', count=True)
def main(verbose):
    if verbose:
        click.echo("Scanning Files")

    directory = os.getcwd()

    rules = flatten_rules(DEFAULT_RULES)

    for filename in os.listdir(directory):
        file_root, file_ext = os.path.splitext(filename)
        file_ext = file_ext.lower()

        if file_ext in rules:
            folder = os.path.join(directory, rules[file_ext])
            if not os.path.exists(folder):
                os.makedirs(folder)

            moveto(filename, directory, folder)

    if verbose:
        click.echo("Done!")


if __name__ == '__main__':
    main()

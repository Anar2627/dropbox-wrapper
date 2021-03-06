import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError


# Dropbox uygulamasını kurma ve Token alma

DROPBOX_ACCESS_TOKEN = 'sl.BIjZ_BNoRGpRsJqED8oMWz7Mp9D3AIf4AnkXwDY4bRvnSyTqwgNn-X8xiN683JJ0zhXqnAZ4p9-mX67Gq-axFSbsRkVx43e6hdgjSDp5aZqUGSf8GWqt4LfzJ6uvQU6Iord5Xb8'



# Dropbox API'sine Bağlanma


def dropbox_connect():
    """Create a connection to Dropbox."""

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx


# Dropbox klasöründeki dosyaların listesini alma


def dropbox_list_files(path):
    """Return a Pandas dataframe of files in a given Dropbox folder path in the Apps directory.
    """

    dbx = dropbox_connect()

    try:
        files = dbx.files_list_folder(path).entries

        files_list = []
        for file in files:

            if isinstance(file, dropbox.files.FileMetadata):

                metadata = {
                    'name': file.name,
                    'path_display': file.path_display,
                    'client_modified': file.client_modified,
                    'server_modified': file.server_modified
                }
                files_list.append(metadata)

        df = pd.DataFrame.from_records(files_list)
        return df.sort_values(by='server_modified', ascending=False)

    except Exception as e:
        print('Error getting list of files from Dropbox: ' + str(e))


print(dropbox_list_files("/Documents"))
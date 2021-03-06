import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError


# Dropbox uygulamasını kurma ve Token alma

DROPBOX_ACCESS_TOKEN = 'sl.BERmUAWHUCBduRQ15CRkYaXHggMeNdP85vb7Ur5U0o3LbVGDJHcub1sfXplqd9l3GRb9omDhKI-bLBqQ0NISyxeIXWHJ0pMtqip1u9wfl1bk1XKgY5FPK4fJ4CdfxT7D6KueGl4'



# Dropbox API'sine Bağlanma


def dropbox_connect():
    """Create a connection to Dropbox."""

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx




# Dropbox'ta bir dosyaya paylaşıla bilir bir bağlantı indirmek



def dropbox_get_link(dropbox_file_path):
    """Get a shared link for a Dropbox file path.

    Args:
        dropbox_file_path (str): The path to the file in the Dropbox app directory.

    Returns:
        link: The shared link.
    """

    try:
        dbx = dropbox_connect()
        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(dropbox_file_path)
        shared_link = shared_link_metadata.url
        return shared_link.replace('?dl=0', '?dl=1')
    except dropbox.exceptions.ApiError as exception:
        if exception.error.is_shared_link_already_exists():
            shared_link_metadata = dbx.sharing_get_shared_links(dropbox_file_path)
            shared_link = shared_link_metadata.links[0].url
            return shared_link.replace('?dl=0', '?dl=1')

dropbox_get_link('/home/Documents/projeno_12.txt')
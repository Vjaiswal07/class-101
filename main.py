import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Hm9cBeuecfEAAAAAAAAAASpXHG3Zq-YvTtdKkPf3_Dd4QpiRD_FhhKo3uOdXyqh0'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to be transfered :")
    file_to = input("enter the file path to upload to dropbox")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved succesfully")   
main()

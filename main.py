from api.get_files import get_files
from api.post_file import post_file


class Pipeline:
    def __init__(self, test_file_path: str):
        self.test_file_path = test_file_path

    def _check_files(self):
        files = get_files()

        if len(files) == 0:
            print("No files found. Uploading test file...")
            post_file(self.test_file_path)

        else:
            print("The following files were found.")
            for file in files:
                print(file["filename"])

    def run(self):
        print("Running pipeline")
        self._check_files()


pipeline = Pipeline("files/Dragon_Language_Print_Dictionary_5th_Edition.pdf")
pipeline.run()

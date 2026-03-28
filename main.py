from api.get_files import get_files
# look for file


# if not found upload file


class Pipeline:
    def _check_files(self):
        files = get_files()

        if len(files) == 0:
            print("No files found. Uploading test file...")
        else:
            print("The following files were found.")

    def run(self):
        print("Running pipeline")
        self._check_files()


pipeline = Pipeline()
pipeline.run()

from api.get_files import get_files
from api.post_file import post_file
from api.get_completion_with_file import get_completion_with_file


class Pipeline:
    def __init__(self, test_file_path: str):
        self.test_file_path = test_file_path

    def _get_prompt(self):
        user_prompt = input("Enter your prompt and press enter: ")
        system_prompt = f"""
Answer all questions in Dovahzul language only. 
A english to Dovahzul dictionary can be found in the provided file page 280 onwards. 
An example translation would be: ability n. suleyk
If the reply in english includes the word 'ability' it should be returned as 'suleyk'.
If you do not know the matching english to Dovahzul translation do not translate.
Do not reply in english. Do not use any english words in the reply. Reply only in Dovahzul.

The below question should be responded to in Dovahzul language only.:
{user_prompt}
"""
        return system_prompt

    def _check_files(self):
        files = get_files()

        if len(files) == 0:
            print("No files found. Uploading test file...")
            post_file(self.test_file_path)
            return self._check_files()

        else:
            print("The following files were found.")
            for file in files:
                print(file["filename"] + "\n")

            print(f'Selecting the first file: {files[0]["filename"]}\n')
            file_id: str = files[0]["id"]
            return file_id

    def _get_reply(self, file_id: str):
        completion = get_completion_with_file(self._get_prompt(), file_id)
        print(completion)

    def run(self):
        print("Running pipeline")
        file_id = self._check_files()
        self._get_reply(file_id)


pipeline = Pipeline("files/Dragon_Language_Print_Dictionary_5th_Edition.pdf")
pipeline.run()

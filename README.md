# Side-by-side Translation Viewer

Well, I've wrote this application in under 3 hours just to conveniently pass the English subject. There is no more functionality than:
- View vocabulary
- View side-by-side original/translated paragraphs of plain imported text

## Usage

To import the data you should firstly create it. It can be done the following way:
1. Create a folder anywhere on your pc
2. Add three files to it (examples can be found in the repo under `example` folder):
    - `_original.txt` - this file should contain the original text, splitted on paragraphs. Example:
        ```
        # Wow, what a nice header!
        ## And this is the secondary header
        Plain text
        ...
        ```
    - `_translation.txt` - this file should have the same number of paragraphs as `_original.txt`. Should contain the translated versions of the paragraphs. Example:
        ```
        # Вот это да, какой классный заголовок!
        ## А это заголовок второго уровня
        Простой текст
        ...
        ```
    - `_vocabulary.txt` - the file, vocabulary data will be parsed from. Should have the following format:
        ```
        <original-word>~<translation>
        <another-original-word>~<another-translation>
        Hello~Привет
        ...
        ```
3. Click the `File -> Open folder` menu item and select the created folder.
4. Now you can see the original text paragraphs side-by-side with the translated versions
5. You might want to view a vocabulary, that we imported. Just click the `File -> Show vocabulary` menu item. The vocabulary window will be created.

## Interface
![image](https://github.com/user-attachments/assets/7fb5881c-7e73-472a-99a1-343ea3f7f3b8)

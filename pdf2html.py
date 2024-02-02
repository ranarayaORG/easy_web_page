import logging
class PDF2HTML:
    FLAGS = {
        "LOGO" : "",
        "MAIL": "",
        "GITHUB": "",
        "LINKEDIN": "",
        "PDF": "",
        "EXTRAOPTIONS": {}
    }

    def __init__(self, html_template, mail, github, linkedin, pdf, extraoptions, logo):
        self.html_template = html_template
        self.FLAGS["LOGO"] = logo
        self.FLAGS["MAIL"] = mail
        self.FLAGS["GITHUB"] = github
        self.FLAGS["LINKEDIN"] = linkedin
        self.FLAGS["PDF"] = pdf
        self.FLAGS["EXTRAOPTIONS"] = extraoptions
        self.html = None
        self.logger = self.setup_logger()

    def setup_logger(self):
        """
        Sets up a logger for logging messages.

        Returns:
            logging.Logger: The logger object.
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('pdf2html.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def generate_html(self):
        """
        Generates an HTML file from a PDF file.

        This method reads an HTML template, replaces flags in the template with actual content,
        and creates an HTML file with the generated content.

        Parameters:
            None

        Returns:
            None
        """
        self.logger.info("Generating HTML file")
        tmp_html = self.read_file(self.html_template)
        tmp_html = self.replace_flags(tmp_html)
        self.create_file_with_string(tmp_html, "index.html")

    def replace_flags(self, html):
        """
        Replaces flags in the HTML string with their corresponding values.

        Args:
            html (str): The HTML string to be processed.

        Returns:
            str: The modified HTML string with flags replaced.

        """
        self.logger.info("Replacing flags in HTML")
        for flag, value in self.FLAGS.items():
            if flag != "EXTRAOPTIONS":
                html = self.replace_substring(html, flag, value)
            else:
                if value:
                    options = self.add_extra_options(value)
                    html = self.replace_substring(html, flag, options)
                else:
                    html = self.replace_substring(html, flag, '')
        return html
    
    def add_extra_options(self, extraoptions):
        """
        Adds extra options to the PDF to HTML converter.

        Parameters:
        extraoptions (dict): A dictionary containing the extra options to be added.

        Returns:
        str: A string representation of the added options.
        """
        self.logger.info("Adding extra options")
        options = []
        for key, value in extraoptions.items():
            option = '<p> <a href="'+ value +'">' + key + '</a> </p>'
            options.append(option)
        res = '\n'.join(options)
        return res
        
    
    def replace_substring(self, string, old_substring, new_substring):
        """
        Replaces occurrences of a substring in a given string with a new substring.

        Parameters:
            string (str): The original string.
            old_substring (str): The substring to be replaced.
            new_substring (str): The new substring to replace the old substring.

        Returns:
            str: The modified string with the replaced substrings.
        """
        self.logger.info("Replacing substring")
        return string.replace(old_substring, new_substring)
        
        
    def read_file(self, file_path):
        """
        Reads the content of a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The content of the file.
        """
        self.logger.info("Reading file")
        with open(file_path, 'r', encoding='latin-1') as file:
            content = file.read()
        return content
    
    def create_file_with_string(self, string, filename):
        """
        Creates a file with a string.

        Args:
            string (str): The string to write to the file.
            filename (str): The name of the file to create.
        """
        self.logger.info("Creating file")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(string)
        self.logger.info("File created successfully")

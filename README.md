# Easy web page

## Description

This project is a simple script that allows you to publish your CV as an HTML webpage. It provides an easy and straightforward way to convert your CV from a PDF format to an HTML format. With just a few lines of code, you can generate a professional-looking webpage that showcases your CV.

The script utilizes the `pdf2html` library and provides options to customize the output, such as specifying the location of your template HTML file, adding links to your GitHub and LinkedIn profiles, and including a logo. Additionally, you can specify extra options like generating SVG images or providing a custom CSS file.

By using this script, you can quickly and effortlessly create an online version of your CV, making it easily accessible and shareable with potential employers or clients.

## Installation

This project does not require any installation. Simply clone the repository and you're ready to go!

## Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Open the project in your preferred code editor.
3. Customize the `template.html` file according to your preferences.
4. Update the `GITHUB_URL` and `LINKEDIN_URL` variables in the code snippet above with your own GitHub and LinkedIn profile URLs.
5. Place your CV in the `data` folder with the filename `cv.pdf`.
6. Run the code snippet above to generate the HTML webpage.

That's it! You have successfully set up and generated your CV as an HTML webpage using this project.

## Usage

```python

from pdf2html import PDFViewer
extraoptions = {
    "svg": "url"
}
pdf_viewer = PDFViewer(r"template.html", "mail", r"GITHUB_URL", r"LINKEDIN_URL", r"data/cv.pdf", extraoptions, r"logo")

pdf_viewer.generate_html()

```
This code snippet demonstrates the usage of the `pdf2html` library to convert a PDF document into an HTML file. Let's break it down step by step:

1. The first line imports the `PDFViewer` class from the `pdf2html` module. This class provides the functionality to convert PDF files to HTML.

2. The second line defines a dictionary called `extraoptions` with a single key-value pair. The key is `"svg"` and the value is `"url"`. These options are used to customize the conversion process. In this case, it specifies that SVG images should be converted using URLs.

3. The third line creates an instance of the `PDFViewer` class. It takes several arguments:
   - The first argument, `r"template.html"`, specifies the path to an HTML template file that will be used to generate the final HTML output.
   - The second argument, `"mail"`, represents the email address that will be displayed in the generated HTML.
   - The third and fourth arguments, `r"GITHUB_URL"` and `r"LINKEDIN_URL"`, represent the URLs for your GitHub and LinkedIn profiles, respectively.
   - The fifth argument, `r"data/cv.pdf"`, is the path to the PDF file that will be converted to HTML.
   - The sixth argument, `extraoptions`, is a dictionary containing additional options for the conversion process.
   - The seventh argument, `r"logo"`, represents the path to a logo image that will be included in the generated HTML.

4. Finally, the `generate_html()` method is called on the `pdf_viewer` object. This method initiates the conversion process and generates the HTML output file based on the provided arguments.

Make sure to replace the placeholder values (`GITHUB_URL`, `LINKEDIN_URL`, etc.) with the actual URLs and file paths relevant to your project.

Feel free to customize the code and the template file to suit your specific needs.

## Hello World

```python
def main():
    extraoptions = {}
    def main():
    pdf_viewer = PDF2HTML(r"template/template.html", "mail", r"https://github.com/", r"https://www.linkedin.com/", r"data/Hello_World.pdf", extraoptions, r"data/Logo.png")

    pdf_viewer.generate_html()
main()
```

## Contributing

Thank you for your interest in contributing to our project! There are several ways you can contribute:

### Creating Templates

If you have expertise in creating templates, you can help us by creating new templates for our project. Templates provide a starting point for others to build upon and can greatly enhance the usability of our project. To contribute a template, follow these steps:

1. Fork the repository.
2. Create a new branch for your template.
3. Design and develop your template, ensuring it meets the project's requirements and guidelines.
4. Test your template to ensure it functions correctly.
5. Submit a pull request, including a detailed description of your template and any relevant documentation.

### Improving the Code

If you have programming skills and want to improve the codebase, you can contribute by submitting code enhancements, bug fixes, or optimizations. To contribute code improvements, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary code modifications, following the project's coding standards and guidelines.
4. Test your changes to ensure they don't introduce any new issues.
5. Submit a pull request, describing the changes you made and the problem they solve.

### Reporting Issues

If you encounter any bugs, have suggestions, or want to request new features, please open an issue on our GitHub repository. Provide as much detail as possible to help us understand and address the problem.

We appreciate all contributions, big or small. Together, we can make our project even better!
## Amharic Information Retrieval Project
### Introduction
This project is an Amharic information retrieval system that consists of the following components:

- Web Spider: A web spider that downloads Amharic files from the internet.
- PDF to Image Conversion: The downloaded PDF files containing text are converted to images.
- Text Operations: The text in the image files is extracted and processed, including tokenization, punctuation removal, normalization, and stemming.
- Statistical Analysis: The processed text is analyzed to verify Zipf's law and Luhn's law.
- Inverted Index: An inverted index is created from the processed text.
- Vector Space Model: The inverted index is used to create a vector space model that employs cosine similarity for information retrieval.
- Search Engine GUI: The search engine provides a user interface that links the query to the relevant websites where the resources were found.

### Usage
- Web Crawling: The web spider component downloads Amharic files from the internet, expanding the corpus for the information retrieval system.
- PDF to Image Conversion: The system processes the downloaded PDF files, converting them to images for further text extraction.
- Text Processing: The text extracted from the image files is tokenized, and punctuation is removed. The text is then normalized, stemmed, and analyzed for statistical properties.
- Inverted Index Creation: The processed text is used to create an inverted index, which is the foundation of the information retrieval system.
- Vector Space Model: The inverted index is used to create a vector space model, which employs cosine similarity to perform information retrieval.
- Search Engine GUI: Users can search for relevant documents using the search engine's graphical user interface. The query is linked to the relevant websites where the resources were found.
### Installation and Setup
- Clone the repository: git clone https://github.com/your-username/amharic-information-retrieval.git
- Install the required dependencies: pip install -r requirements.txt
- Configure the necessary settings, such as the web crawling parameters and the file storage locations.
- Run the web crawler, text processing, and information retrieval components.
- Start the search engine GUI.
### Contributions
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.

### Example
- While searching for `ፍቅር እስከ መቃብር` the result will appear as the screenshots below and when you click the result in the GUI it will take you to the website.
![image](https://github.com/Yosef-ft/Amharic_IR_System/assets/143919830/086419c2-e3a5-4f1e-b8ff-37aa9d89f32f)

License
This project is licensed under the MIT License.

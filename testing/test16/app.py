"""
make the main app for the website 

"""
#imports
import json
from flask import Flask, render_template,abort

from read_data_mongo import get_article_data

#for test 
import json

#const

#db names in mongo
db_name = ["articles","section"]

#collection names in database 
collections = ["projects","section_data"]


app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/<section_name>')
def section(section_name):

    page_data = get_article_data(db_name[1],collections[1],{'section_name': section_name})

    print(page_data)

    return render_template('section.html',**page_data)


@app.route('/projects/<article_name>')
def article(article_name):


    data = get_article_data(db_name[0],collections[0],{'article_name': article_name}) 

    page_data = {"articles_json": data}

    return render_template('projects/article.html', **page_data)


@app.route('/dummy')
def dummy():
    articles_json = {
        "article_name": "patching-unpatching",
        "aticle_data": [
            
            {"title": "Patching Unpatching Open Source tool", "image_src": "..\\static\\images\\projects\\patching-unpatching\\patching.png", "article_para": "", "markdown_data": ""},
            {"title": "Project Description", "image_src": "", "article_para": "", "markdown_data": ""},
            {"title": "", "image_src": "", "article_para": "Patching and Unpatching are a set of tools that are used for image processing. The patching tool is used to cut small square sections of the input image known as patches. The unpatching tool takes those patches and combines them back together to make the final image.", "markdown_data": ""},
            {"title": "", "image_src": "", "article_para": "", "markdown_data": "### Patching Tool"},
            {"title": "", "image_src": "", "article_para": "Patching is the initial step in the image processing pipeline, responsible for dividing the input image into smaller, manageable sections called patches. These patches are typically square-shaped and can vary in size based on user-defined parameters such as patch size and padding.", "markdown_data": ""},
            {"title": "", "image_src": "", "article_para": "", "markdown_data": "**Key Features:**\n1. **Segmentation:** The patching tool effectively segments the input image, breaking it down into discrete patches. This segmentation enables localized analysis and processing, facilitating tasks such as feature extraction and object detection.\n2. **Padding Options:** To ensure consistency and accuracy during patch extraction, the patching tool offers padding options such as reflective padding. This padding technique extends the borders of the image by replicating pixel values, thereby maintaining continuity across patch boundaries.\n3. **Support for Multiple Image Types:** Whether dealing with grayscale (single-channel) or color (three-channel) images, the patching tool accommodates diverse image types. This flexibility extends its utility across various applications, from medical imaging to satellite imagery analysis.\n4. **Parameter Customization:** Users have the flexibility to customize parameters such as patch size and padding width to suit specific requirements. Fine-tuning these parameters enables optimization for different image characteristics and processing objectives."},
            {"title": "", "image_src": "", "article_para": "", "markdown_data": "### Unpatching Tool"},
            {"title": "", "image_src": "..\\static\\images\\projects\\patching-unpatching\\unpatching.png", "article_para": "", "markdown_data": ""},
            {"title": "", "image_src": "", "article_para": "Following patching, the Unpatching tool plays a crucial role in reconstructing the original or modified image from the segmented patches. It operates in conjunction with Patching, leveraging the extracted patch information to generate a cohesive image representation.", "markdown_data": ""},
            {"title": "", "image_src": "", "article_para": "", "markdown_data": "**Key Features:** \n1. **Reconstruction:** The primary function of the Unpatching tool is to reconstruct the original image from the segmented patches. By combining these patches in a systematic manner, it restores the spatial integrity and continuity of the image.\n2. **Scalability:** The Unpatching tool offers scalability, allowing for both image enlargement and reduction. This capability is particularly useful in applications requiring image upscaling or downscaling while preserving visual fidelity.\n3. **Parameter Consistency:** To ensure consistency with the patching process, the Unpatching tool maintains compatibility with parameters such as patch size and padding width. This consistency facilitates seamless integration into the overall image processing workflow.\n4. **Enhanced Flexibility:** Beyond basic reconstruction, the Unpatching tool supports advanced functionalities such as blown upscale. This feature enables the user to specify the degree of enlargement or scaling applied to the reconstructed image, enhancing flexibility and control."},
            {"title": "", "image_src": "", "article_para": "", "markdown_data": "### Integration and Workflow"},
            {"title": "", "image_src": "", "article_para": "The seamless integration of Patching and Unpatching forms a comprehensive image processing workflow. Following patch extraction, the resulting patches can undergo various analyses or modifications before being fed into the Unpatching tool for reconstruction. This integrated approach streamlines the processing pipeline, offering efficiency, flexibility, and robustness.", "markdown_data": ""},
            {"title": "", "image_src": "", "article_para": "In summary, Patching and Unpatching represent indispensable components of modern image processing frameworks. Their ability to segment, analyze, and reconstruct images empowers researchers, engineers, and practitioners across diverse domains, driving innovation and advancement in computer vision and image analysis.", "markdown_data": ""},

            

        ],
        "card_one_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_one": "..\\static\\images\\misc\\cards.jpg",
        "card_first_url": "https://www.meabhi.me",
        "card_two_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_two": "..\\static\\images\\misc\\cards.jpg",
        "card_three_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_three": "..\\static\\images\\misc\\cards.jpg"
    }

    page_data = {"articles_json": articles_json}

    return render_template('projects/article.html', **page_data)





if __name__ == '__main__':
    app.run(debug=True)
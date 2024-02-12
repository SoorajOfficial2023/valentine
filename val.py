from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result/<int:page_number>')
def result(page_number):
    if page_number == 0:
        message = 'I LOVE YOU 😍'
        color = 'red'
        image_filename = 'love_image.jpg'  # Replace with the actual filename for the "I LOVE YOU" image
        return render_template('result.html', message=message, color=color, image_filename=image_filename)
    elif 1 <= page_number <= 5:
        messages = [
            "Don't say that...",
            "It's hurting...",
            "Please, don't...",
            "I'll cry...",
            "This is painful..."
        ]
        message = messages[page_number - 1]
        image_filenames = [
            'image1.png',  
            'image2.png',  
            'image3.png',  
            'image4.png','image5.png'  
               
        ]
        image_filename = image_filenames[page_number - 1]
        if page_number == 5:
            return render_template('final.html')
        else:
            return render_template('no.html', message=message, page_number=page_number + 1, image_filename=image_filename)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

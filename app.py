from flask import Flask, render_template, request, g
from scrape import extract_information
import similarity_matching

app = Flask(__name__)

# Index route
@app.route('/', methods=['GET', 'POST'])
def index():
    global detail_dict
    if request.method == 'POST':
        url = request.form['url']

        result = extract_information(url)

        if(result == 1):
            result_display = "Error: Connection could not be established."
            return render_template('index.html', result_display=result_display)
        
        elif(result == 2):
            result_display = "Error: Too many requests. Please try again later."
            return render_template('index.html', result_display=result_display)
        
        else:
            detail_dict = result
            return render_template('search.html')

    else:
        return render_template('index.html')


def match(text):
    global detail_dict 
    global result_display

    # args - query, specification dictionary, returns - list [name, detail]
    result = similarity_matching.search(text, detail_dict)
    if result[0] == "0":
            result_display = "No results found."
    else:
        specification_name = result[0]
        specification_detail = result[1]

        # Convert to displaying format
        result_display = specification_name + ": " + specification_detail
    
    return result_display


# 'Search specification' page
@app.route('/search', methods=['GET', 'POST'])
def search():
    global result_display
    if request.method == 'POST':
        text = request.form['search']
        result_display = match(text)
        
    return render_template('search.html', result_display=result_display)    


# 'How-it-works' page
@app.route('/working')
def working():
    return render_template('working.html')


# Display errors in p tags instead of throwing
@app.errorhandler(Exception)
def all_exception_handler(error):
   result_display = "Error: " + str(error)
   return render_template('index.html', result_display=result_display)


if __name__ == '__main__':
    app.run(debug=True)
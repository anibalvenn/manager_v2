from flask import render_template, request, redirect, url_for
from app.services.main import start_championship
from app.services.main import build_ranked_series
from app.services.main import add_series_to_ranking

def init_routes(app):
    

  @app.route('/start-championship', methods=['POST'])
  def handle_start_championship():
    num_series = int(request.form['num_series'])
    num_random_series = int(request.form['num_random_series'])
    championship_name = request.form['championship_name']
    
    start_championship(num_series, num_random_series, championship_name)
    return redirect(url_for('home'))  # Assuming 'home' is the view function for your index page.
      
  @app.route('/', methods=['GET', 'POST'])
  def home():

    if request.method == 'POST':
        number = int(request.form['number'])
        result = number * 5
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

  @app.route('/handle-ranked-series', methods=['POST'])
  def handle_ranked_series():
      data = request.json  # Parse JSON data from the request body
      if data and 'fileName' in data:
          file_name = data['fileName']
          print('Ranked series file name:', file_name)
          build_ranked_series(file_name)

          # Now you have the file name, you can process it further

          return 'File name received successfully', 200
      else:
          return 'No file name provided', 400
      
  @app.route('/handle-add-results', methods=['POST'])
  def handle_add_results():
      data = request.json  # Parse JSON data from the request body
      if data and 'fileName' in data:
          file_name = data['fileName']
          path_file_name =  "C:/Users/User/Documents/skat/manager_v2/db/championships/Paulista/"+file_name
          print('Add results file name:', path_file_name)
          add_series_to_ranking(path_file_name)

          # Now you have the file name, you can process it further

          return 'Add results file name received successfully', 200
      else:
          return 'No add results file name file name provided', 400
      
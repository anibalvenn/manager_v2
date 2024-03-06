from flask import render_template, request, redirect, url_for
from app.services.start_championship import start_championship

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

    

    






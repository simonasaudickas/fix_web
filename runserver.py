
import subprocess

def activate_venv():
    activate_command = r'fix\Scripts\activate'
    subprocess.call(activate_command, shell=True)

# Call the function to activate the virtual environment
activate_venv()
from waitress import serve
from mysite.wsgi import application

if __name__ == '__main__':
    serve(application, host ='localhost', port='8081')
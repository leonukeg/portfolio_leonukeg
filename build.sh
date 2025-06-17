python -m venv venv    
.\venv\Scripts\activate
pip install reflex     
reflex init          
reflex export --frontend-only
rm -fr public
unzip frontend.zip -d public
rm -Force frontend.zip
deactivate
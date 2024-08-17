@echo off
echo Creating files...
type nul > app.py
type nul > models.py
type nul > forms.py
type nul > recommendations.py
type nul > __init__.py
mkdir templates
type nul > templates\survey.html
type nul > templates\recommendations.html
echo Done!

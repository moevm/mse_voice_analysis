install:
	sudo apt install python3-pip
	pip3 install pyinstaller
	python3 -m PyInstaller ./src/main.py -F
	sudo cp ./dist/main /usr/local/bin/mse_voice_analysis

clearbuild:
	rm -rf dist/ build/ main.spec src/__pycache__/ 
	
uninstall:
	sudo rm -f /usr/local/bin/mse_voice_analysis

install:
	sudo apt install python3-pip
	pip3 install pyinstaller
	python3 -m PyInstaller ./MSE_VOICE_ANALYSIS/'Iteration 1'/main.py -F
	sudo cp ./dist/main /usr/local/bin/mse_voice_analysis

clearbuild:
	rm -rf dist/ build/ main.spec MSE_VOICE_ANALYSIS/'Iteration 1'/__pycache__/ 
	
uninstall:
	rm -f /usr/local/bin/mse_voice_analysis

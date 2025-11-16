## Home Assistant AI
### Explanation
Using gemma3:1b and SpeechRecognition, this AI is prompted through human speech and generate 2 output, normal converstation and JSON that represent object with the state. <br>
<br>
This code run three things, 
<ol>
  <li>using SpeechRecognition to capture your speech from your device microphone and send it to Houndify for processing your speech to text</li>
  <li>Then, the text from speech will be directed to the customized AI from Ollama using the Modelfile. Then the AI will generate an output.</li>
  <li>the output from the AI will go through a catcher function to ensure proper formatting and cleaning.</li>
</ol>
<br>
  
### How to Install and run
<b> 1. Clone this Repository to your machine</b>

<b> 2. Ollama</b>
<ul>
  <li>Go to the <a href="https://ollama.com/">Ollama official website</a> and download the Ollama</li>
  <li>Install the Ollama as instructed depending on your machine</li>
  <li>check if Ollama has been installed by typing "ollama" to your terminal </li>
  <li>run <b>"ollama create boolean -f ModelFile"</b> inside the cloned repository to build the model</li>
  <li>run <b>"ollama serve"</b> to initiate Ollama services </li>
</ul>
<b> 3. Houndify</b>
<ul>
  <li>Go to the <a href="https://www.houndify.com/signup">Houndify official signup website</a> and sign yourself to get the API keys</li>
  <li>After signing up, go to the dashboard of your houndify account</li>
  <li>Go to your client and you will see both <b>Client Id</b> and <b>Client Key</b></li>
</ul>
<b>4. Starting the script</b>
<ul>
  <li>Replace the <b>secret.py.example</b> credential from the cloned repository with your own</li>
  <li>remove the <b>.example</b> extension so the file becomes <b>secret.py</b></li>
  <li>run the <b>script.py</b> and start talking!</li>
</ul>

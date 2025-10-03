<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
 </head>
<body>

<h1>🚀 Endpoint Detection and Response (EDR) Tool</h1>

<h2>📌 Overview</h2>

<p>
    The <b>Endpoint Detection and Response (EDR) Tool</b> is a lightweight security solution designed to monitor system processes in real time 
    and detect potentially malicious activity. It identifies and logs suspicious processes that may indicate unauthorized access, malware infections, 
    or cyberattacks. The tool is highly efficient and can be deployed on multiple endpoints with minimal system impact.
</p>

<h3>* Key Capabilities:</h3>
<ul>
    <li> <b>Real-Time Process Monitoring:</b> Continuously tracks running processes.</li>
    <li> <b>Suspicious Process Detection:</b> Detects known hacking tools and malware.</li>
    <li> <b>Incident Logging:</b> Records detection events for forensic analysis.</li>
    <li> <b>Lightweight Deployment:</b> Minimal system impact with no performance degradation.</li>
    <li> <b>Extensibility:</b> Allows custom rules and suspicious process definitions.</li>
</ul>

<h2>* Key Features</h2>

<h3>* Real-Time Process Monitoring</h3>
<ul>
    <li>Monitors all running processes in real time.</li>
    <li>Utilizes <b>psutil</b> library for efficient process scanning.</li>
    <li>Collects process details including <b>PID, executable path, and CPU usage</b>.</li>
</ul>

<h3>* Suspicious Process Detection</h3>
<ul>
    <li>Identifies known hacking tools and reconnaissance software such as:</li>
    <ul>
        <li> <b>netcat</b> - Often used for backdoor access.</li>
        <li> <b>nmap</b> - Network scanning tool.</li>
        <li> <b>hydra</b> - Brute-force attack tool.</li>
    </ul>
    <li>Alerts security teams when a match is found.</li>
</ul>

<h3>* Incident Logging</h3>
<ul>
    <li>Records every detection event to a structured log file.</li>
    <li>Stores details such as <b>timestamp, process name, and user</b> running the process.</li>
</ul>

<h3>* Lightweight and Efficient</h3>
<ul>
    <li>Consumes minimal CPU and RAM resources.</li>
    <li>Can run as a background service or scheduled task.</li>
</ul>

<h3>* Extensibility</h3>
<ul>
    <li>Supports adding new suspicious process names dynamically.</li>
    <li>Can be integrated with a <b>SIEM system</b> for centralized monitoring.</li>
</ul>

<h2>📥 Installation</h2>

<h3>* Prerequisites</h3>
<ul>
    <li>Python <b>3.8+</b> is required.</li>
    <li>Install dependencies using <code>pip</code>:</li>
</ul>

<pre>
<code>pip install psutil</code>
</pre>

<h3>* Clone the Repository</h3>
<pre>
<code>git clone https://github.com/yourusername/Cybersecurity-Portfolio.git
cd Cybersecurity-Portfolio/6_Endpoint_Detection_Response</code>
</pre>

<h2>⚙️ Configuration</h2>

<table border="1">
    <tr>
        <th>Setting</th>
        <th>Description</th>
        <th>Default Value</th>
    </tr>
    <tr>
        <td><b>Monitored Processes</b></td>
        <td>List of suspicious processes to detect.</td>
        <td>["netcat", "nmap", "hydra"]</td>
    </tr>
    <tr>
        <td><b>Log File</b></td>
        <td>Location where logs are stored.</td>
        <td>edr_logs.txt</td>
    </tr>
</table>

<h2> Usage</h2>

<h3>1- Start the EDR Tool</h3>
<p>To begin monitoring system processes:</p>
<pre>
<code>python edr.py --monitor</code>
</pre>

<h3>2- Query the Log File</h3>
<p>To search for previous detections:</p>
<pre>
<code>python edr.py --query</code>
</pre>

<h3>3- Add New Suspicious Process</h3>
<p>To dynamically update the detection list:</p>
<pre>
<code>python edr.py --add-process "malicious.exe"</code>
</pre>

<h2>* Architecture Overview</h2>

<p>The <b>Endpoint Detection and Response (EDR) Tool</b> consists of multiple modular components:</p>

<ul>
    <li><b> Process Monitoring Engine:</b> Continuously checks running processes.</li>
    <li><b> Detection Module:</b> Matches process names against a suspicious list.</li>
    <li><b> Logging Module:</b> Records detection details in a log file.</li>
    <li><b> Configuration Manager:</b> Allows dynamic updates to detection rules.</li>
</ul>

<p> <b>Architecture Diagram:</b> See <b>docs/architecture.png</b> for details.</p>

<h2>- Sample Output</h2>

<h3>📄 EDR Log Example:</h3>

<pre>
[2024-02-14 15:45:20] ALERT: Suspicious process detected - netcat (PID: 2890)
[2024-02-14 15:46:02] ALERT: Suspicious process detected - hydra (PID: 3102)
</pre>

<h3>📈 EDR Detection Report:</h3>
<p> See <b>docs/sample_edr_log.png</b> for real log screenshots.</p>

<h2> Contributing</h2>

<p> Contributions are welcome! If you'd like to contribute:</p>

<ol>
    <li>Fork the repository.</li>
    <li>Create a feature branch.</li>
    <li>Commit changes following best practices.</li>
    <li>Submit a pull request.</li>
</ol>

<p> Ensure that your code follows <b>PEP8</b> guidelines and includes <b>unit tests</b> before submitting.</p>


<h2>** Developed for security professionals, SOC teams, and IT administrators.</h2>
<h3>Enhance Endpoint Security with EDR! 🔥</h3>

</body>
</html>

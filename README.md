# 🚀 Flask System Info Viewer

This simple Flask application dynamically displays essential system information about its runtime environment (whether it's a Docker container or a direct server) on an HTML page. This includes IP address, hostname, operating system details, CPU, and memory usage.

---

## ✨ Features

* **Client Information:** Displays the IP address and resolvable hostname of the requesting client.
* **Backend System Information:**
    * Hostname and IP address of the server (or container) where the application is running.
    * Operating system name, version, kernel version, and architecture.
    * Python version.
    * System uptime.
    * Number of CPU cores.
    * **Live CPU Usage Percentage.**
    * **Total, Used, and Percentage Memory Usage.**
* **Container-Friendly:** Works seamlessly in containerized environments like Docker, accurately reporting resources allocated/used by the container.
* **Simple & Lightweight:** Quick setup and execution with minimal dependencies.

---

## 🛠️ Setup & Running

### Dependencies

* Python 3.x
* Flask
* psutil

### Running Locally

1.  Clone the repository:
    
    ```bash
    git clone [https://github.com/mustafaUrl/sys-info.git](https://github.com/mustafaUrl/sys-info.git)
    ```
    ```bash
    cd sys-info
    ```
    
2.  Create and activate a Python virtual environment (recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Start the application:
    ```bash
    python app.py
    ```
5.  Open your browser and navigate to `http://127.0.0.1:5000`.

### Running with Docker

This application can also be run as a Docker image, making deployment incredibly easy.

1.  Ensure you have Docker installed and running on your system.
2.  **Pull the Docker image:**
    ```bash
    docker pull uraler/sys-info:latest
    ```
3.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 uraler/sys-info:latest
    ```
4.  Open your browser and navigate to `http://localhost:5000`.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🤝 Contributing

Contributions are always welcome! If you find bugs, want to add new features, or suggest improvements, feel free to open an [issue](https://github.com/mustafaUrl/sys-info/issues) or submit a [pull request](https://github.com/mustafaUrl/sys-info/pulls).

---


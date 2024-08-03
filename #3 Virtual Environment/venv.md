# Python Virtual Environment Setup

This guide provides a straightforward approach to creating and managing a Python virtual environment for your projects.

## Prerequisites

- Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Steps to Create a Virtual Environment

1. **Open your Terminal or Command Prompt.**

2. **Navigate to your project directory:**

   ```bash
   cd /path/to/your/project
   ```

3. **Create a virtual environment:**

   For Python 3:

   ```bash
   python -m venv env
   ```

   For Python 2 (optional, as Python 2 is end-of-life):

   ```bash
   virtualenv env
   ```

   Here, `env` is the name of the virtual environment. You can choose a different name if you prefer.

4. **Activate the virtual environment:**

   - On **Windows:**

     ```bash
     .\env\Scripts\activate
     ```

   - On **macOS and Linux:**

     ```bash
     source env/bin/activate
     ```

   After activation, you should see `(env)` before your command prompt, indicating that the virtual environment is active.

5. **Install packages within the virtual environment:**

   Use `pip` to install packages:

   ```bash
   pip install package_name
   ```

   Replace `package_name` with the name of the package you wish to install.

6. **Deactivate the virtual environment:**

   When you are done working in the virtual environment, you can deactivate it by running:

   ```bash
   deactivate
   ```

## Additional Information

- To **remove** the virtual environment, simply delete the `env` directory.

- For a **requirements file**, you can generate it with:

  ```bash
  pip freeze > requirements.txt
  ```

  And install packages from it with:

  ```bash
  pip install -r requirements.txt
  ```

Feel Free to visit [NetHyTech](https:/www.youtube.com/@nethytech)

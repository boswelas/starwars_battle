# Use the official Playwright image
FROM mcr.microsoft.com/playwright/python:v1.28.1-focal

WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install Playwright browsers
RUN python -m playwright install

# Command to run the application
CMD ["gunicorn", "app.main:app"]

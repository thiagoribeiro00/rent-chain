# Use a base image for Python
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY . .

# Install streamlit
RUN pip install streamlit

# Expose the port
EXPOSE 4000

# Run the command to start the Streamlit app when the container launches
CMD ["streamlit", "run", "main.py", "--server.port=4000", "--server.address=0.0.0.0"]

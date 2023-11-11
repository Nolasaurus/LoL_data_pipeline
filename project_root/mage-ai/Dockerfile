# Use the mageai/mageai image as a base
FROM mageai/mageai

# Set the working directory in the Docker image
WORKDIR /home/src

# Expose port 6789
EXPOSE 6789

# Copy local code to the container image
COPY . /home/src/

# Set the command to run when starting the container
CMD ["/app/run_app.sh", "mage", "start", "lol_data_pipeline"]

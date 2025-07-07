# Download Postman .tar.gz file

# Extract .tar.gz file
```
  tar -xvzf filename.tar.gz
```

# Copy the directory to .local/src/
```
  cp -r ./Postman/ ~/.local/src/
```

# Create symlink to the postman executable
```
  sudo ln -s /home/$USER/.local/src/Postman/Postman /usr/bin/
```
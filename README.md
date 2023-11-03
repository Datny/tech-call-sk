# tech-call-sk
## !! Important !! - docker-compose-yml for this project don't check if DB got before APP, so it's safer to first run 
docker-compose up db-sk  and follow that by either: <br>
docker-compose up <br>
or <br>
docker-compose up app-sk

### Disclaimer: I'm aware that most configuration files could be moved to pyproject.toml
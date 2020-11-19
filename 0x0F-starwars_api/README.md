# 0x0F. Star Wars API

## Resources

* https://github.com/standard/semistandard
* https://github.com/request/request
* https://swapi-api.hbtn.io/

## More Info

### Install Node 10

```sh
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

```sh
$ sudo npm install semistandard --global
```

### Install request module and use it

```sh
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Task

### 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: 3 = �Return of the Jedi�
- Display one character name per line in the same order as the �characters� list in the /films/ endpoint
- You must use the Star wars API
- You must use the request module

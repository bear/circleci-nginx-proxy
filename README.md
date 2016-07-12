A test Python Flask app to show how to have Nginx act as a proxy-forward inside of a CircleCI build.

## Requirements and Assumptions
- Python v2.7
- Python Flask
- Nginx

## Nginx Config

```
server {
    listen      80;
    server_name _;

    location / {
        try_files $uri @flask;
    }
    location @flask {
        proxy_pass         http://localhost:5000;
        proxy_redirect     off;
        proxy_set_header   Host "foobar.com";
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Host $server_name;
    }
}
```

## Running
```
make server
```

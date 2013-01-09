## Collector

A simple API server that does one thing; collects JSON. Multiple API endpoints/resources/paths can be configured, each with it's own MongoDB backend. It's effectively an API router for persisting JSON to multiple MongoDB databases and/or collections.


### Installation & usage

Setup the virtual env and install dependencies:

```
$ virtualenv env
$ . env/bin/activate
$ pip install -r requirements.txt
```

Edit the `config.yml` file to suit your needs and then either deploy the WSGI file 
or run `python src/server.py`. See the usage example provided in `example/` for an idea
on how things should work out.


### License

Simplified BSD. See the LICENSE file for further information.

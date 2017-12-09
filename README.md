VS API
======
Very special value store API for setting and retrieving key value pairs

# Development
## Setting up your local environment
```
cd value_store_api
virtualenv venv
source venv/bin/activate
```

## Running the API locally
```
pip install -r requirements.txt
export FLASK_DEBUG=1  # use debug mode for code auto-reloading
python app.py
```

## Running tests
```
pip install -r requirements.txt
./scripts/test
```

# Interface
## /set
Write arbitrary key value pairs to storage

### parameters
Any key value pair

### example request
```
GET /set?candace towns=oklahoma&breyanna stevenson=georgia
```

### example response
the number of key value pairs added to storage
```
{
    'count': 2
}
```

## /get
Retrieve values for a list of keys

### parameters
##### keys (required)
Comma-separated list of keys

### example request
```
GET /get?keys=candace towns,breyanna stevenson,stephanie montez
```

### example response
note: null values are returned for missing keys
```
{
    'candace towns': 'oklahoma',
    'breyanna stevenson': 'georgia',
    'stephanie montez': null
}
```

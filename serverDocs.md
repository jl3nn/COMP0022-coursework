---
title: A swagger API v0.0.1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="a-swagger-api">A swagger API v0.0.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

powered by Flasgger

<h1 id="a-swagger-api-autocomplete">Autocomplete</h1>

## get__autocomplete_genre

> Code samples

```shell
# You can also use wget
curl -X GET /autocomplete/genre?prefix=string \
  -H 'Accept: application/json'

```

```http
GET /autocomplete/genre?prefix=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/autocomplete/genre?prefix=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/autocomplete/genre',
  params: {
  'prefix' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/autocomplete/genre', params={
  'prefix': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/autocomplete/genre', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/autocomplete/genre?prefix=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/autocomplete/genre", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /autocomplete/genre`

Autocomplete endpoint for genre names based on a search query.

<h3 id="get__autocomplete_genre-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|prefix|query|string|true|The search prefix for autocomplete.|

> Example responses

> A list of genres matching the search query.

```json
[
  "Comedy",
  "Drama",
  "Action"
]
```

<h3 id="get__autocomplete_genre-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of genres matching the search query.|None|

<h3 id="get__autocomplete_genre-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get__autocomplete_movie

> Code samples

```shell
# You can also use wget
curl -X GET /autocomplete/movie?prefix=string \
  -H 'Accept: application/json'

```

```http
GET /autocomplete/movie?prefix=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/autocomplete/movie?prefix=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/autocomplete/movie',
  params: {
  'prefix' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/autocomplete/movie', params={
  'prefix': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/autocomplete/movie', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/autocomplete/movie?prefix=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/autocomplete/movie", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /autocomplete/movie`

Autocomplete endpoint for movie titles based on a search query.

<h3 id="get__autocomplete_movie-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|prefix|query|string|true|The search prefix for autocomplete.|

> Example responses

> A list of movie titles matching the search query.

```json
[
  "Inception",
  "The Matrix",
  "Interstellar"
]
```

<h3 id="get__autocomplete_movie-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of movie titles matching the search query.|None|

<h3 id="get__autocomplete_movie-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get__autocomplete_search

> Code samples

```shell
# You can also use wget
curl -X GET /autocomplete/search?prefix=string \
  -H 'Accept: application/json'

```

```http
GET /autocomplete/search?prefix=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/autocomplete/search?prefix=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/autocomplete/search',
  params: {
  'prefix' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/autocomplete/search', params={
  'prefix': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/autocomplete/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/autocomplete/search?prefix=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/autocomplete/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /autocomplete/search`

Combined autocomplete endpoint for movies, actors, and directors based on a search query.

<h3 id="get__autocomplete_search-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|prefix|query|string|true|The search prefix for autocomplete.|

> Example responses

> A combined list of movies, actors, and directors matching the search query.

```json
{
  "actors": [
    "Leonardo DiCaprio"
  ],
  "directors": [
    "Christopher Nolan"
  ],
  "movies": [
    "Inception"
  ]
}
```

<h3 id="get__autocomplete_search-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A combined list of movies, actors, and directors matching the search query.|None|

<h3 id="get__autocomplete_search-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get__autocomplete_tag

> Code samples

```shell
# You can also use wget
curl -X GET /autocomplete/tag?prefix=string \
  -H 'Accept: application/json'

```

```http
GET /autocomplete/tag?prefix=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/autocomplete/tag?prefix=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/autocomplete/tag',
  params: {
  'prefix' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/autocomplete/tag', params={
  'prefix': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/autocomplete/tag', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/autocomplete/tag?prefix=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/autocomplete/tag", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /autocomplete/tag`

Autocomplete endpoint for tag names based on a search query.

<h3 id="get__autocomplete_tag-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|prefix|query|string|true|The search prefix for autocomplete.|

> Example responses

> A list of tags matching the search query.

```json
[
  "mind-bending",
  "dream",
  "subconscious"
]
```

<h3 id="get__autocomplete_tag-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of tags matching the search query.|None|

<h3 id="get__autocomplete_tag-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get__autocomplete_user

> Code samples

```shell
# You can also use wget
curl -X GET /autocomplete/user?prefix=string \
  -H 'Accept: application/json'

```

```http
GET /autocomplete/user?prefix=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/autocomplete/user?prefix=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/autocomplete/user',
  params: {
  'prefix' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/autocomplete/user', params={
  'prefix': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/autocomplete/user', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/autocomplete/user?prefix=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/autocomplete/user", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /autocomplete/user`

Autocomplete endpoint for user IDs based on a search query.

<h3 id="get__autocomplete_user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|prefix|query|string|true|The search prefix for autocomplete.|

> Example responses

> A list of user IDs matching the search query.

```json
[
  1,
  2,
  3
]
```

<h3 id="get__autocomplete_user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of user IDs matching the search query.|None|

<h3 id="get__autocomplete_user-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-cache-management">Cache Management</h1>

## get__caching_flush

> Code samples

```shell
# You can also use wget
curl -X GET /caching/flush \
  -H 'Accept: application/json'

```

```http
GET /caching/flush HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/caching/flush',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/caching/flush',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/caching/flush', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/caching/flush', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/caching/flush");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/caching/flush", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /caching/flush`

Clears the application cache, flushing all stored data.

> Example responses

> Confirmation message that the cache has been flushed.

```json
{
  "message": "Cache flushed"
}
```

<h3 id="get__caching_flush-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Confirmation message that the cache has been flushed.|None|

<h3 id="get__caching_flush-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-testing">Testing</h1>

## get__caching_test

> Code samples

```shell
# You can also use wget
curl -X GET /caching/test \
  -H 'Accept: application/json'

```

```http
GET /caching/test HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/caching/test',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/caching/test',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/caching/test', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/caching/test', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/caching/test");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/caching/test", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /caching/test`

A test endpoint to fetch a limited set of movie data for testing database connection and query execution.

> Example responses

> A limited list of movie data including various attributes such as image URL, title, year, average rating, genres, tags, ratings, actors, and directors.

```json
[
  {
    "actors": [
      "Leonardo DiCaprio",
      "Joseph Gordon-Levitt"
    ],
    "directors": [
      "Christopher Nolan"
    ],
    "genres": [
      "Action",
      "Adventure",
      "Sci-Fi"
    ],
    "imageUrl": "http://example.com/image.jpg",
    "rating": 8.8,
    "ratings": [
      9,
      8,
      10,
      7
    ],
    "tags": [
      "mind-bending",
      "dream",
      "subconscious"
    ],
    "title": "Inception",
    "year": 2010
  }
]
```

<h3 id="get__caching_test-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A limited list of movie data including various attributes such as image URL, title, year, average rating, genres, tags, ratings, actors, and directors.|None|

<h3 id="get__caching_test-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-genres">Genres</h1>

## get__genres_controversial

> Code samples

```shell
# You can also use wget
curl -X GET /genres/controversial \
  -H 'Accept: application/json'

```

```http
GET /genres/controversial HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/genres/controversial',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/genres/controversial',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/genres/controversial', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/genres/controversial', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/genres/controversial");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/genres/controversial", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /genres/controversial`

Retrieves genres sorted by the standard deviation of their ratings to identify the most controversial genres.

> Example responses

> A list of controversial genres based on the standard deviation of ratings.

```json
[
  {
    "genre": "Horror",
    "statistic": 2.1
  },
  {
    "genre": "Sci-Fi",
    "statistic": 2
  }
]
```

<h3 id="get__genres_controversial-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of controversial genres based on the standard deviation of ratings.|None|

<h3 id="get__genres_controversial-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get__genres_popular

> Code samples

```shell
# You can also use wget
curl -X GET /genres/popular \
  -H 'Accept: application/json'

```

```http
GET /genres/popular HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/genres/popular',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/genres/popular',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/genres/popular', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/genres/popular', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/genres/popular");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/genres/popular", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /genres/popular`

Retrieves genres sorted by their average ratings to identify the most popular genres.

> Example responses

> A list of popular genres based on average ratings.

```json
[
  {
    "genre": "Comedy",
    "statistic": 4.5
  },
  {
    "genre": "Drama",
    "statistic": 4.3
  }
]
```

<h3 id="get__genres_popular-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of popular genres based on average ratings.|None|

<h3 id="get__genres_popular-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## post__genres_user-preferences

> Code samples

```shell
# You can also use wget
curl -X POST /genres/user-preferences \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /genres/user-preferences HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "opinion": 1
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/genres/user-preferences',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/genres/user-preferences',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/genres/user-preferences', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/genres/user-preferences', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/genres/user-preferences");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/genres/user-preferences", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /genres/user-preferences`

Retrieves genres based on user preference for high, low, or mid-range rated movies, indicated by the opinion value.

> Body parameter

```json
{
  "opinion": 1
}
```

<h3 id="post__genres_user-preferences-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|JSON payload containing the user opinion on movie ratings.|
|» opinion|body|integer|true|User opinion indicating preference. 1 for high-rated (4 to 5), 2 for low-rated (0 to 2), any other value for mid-range rated (2 to 4) movies.|

> Example responses

> A list of genres based on the specified user preference.

```json
[
  {
    "genre": "Adventure",
    "preference": 4.5
  },
  {
    "genre": "Action",
    "preference": 4.7
  }
]
```

<h3 id="post__genres_user-preferences-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of genres based on the specified user preference.|None|

<h3 id="post__genres_user-preferences-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-movie-details">Movie Details</h1>

## get__movies_get-by-id

> Code samples

```shell
# You can also use wget
curl -X GET /movies/get-by-id?movieId=0 \
  -H 'Accept: application/json'

```

```http
GET /movies/get-by-id?movieId=0 HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/movies/get-by-id?movieId=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/movies/get-by-id',
  params: {
  'movieId' => 'integer'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/movies/get-by-id', params={
  'movieId': '0'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/movies/get-by-id', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/movies/get-by-id?movieId=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/movies/get-by-id", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /movies/get-by-id`

Retrieves detailed information for a specific movie by its ID.

<h3 id="get__movies_get-by-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|movieId|query|integer|true|The ID of the movie to retrieve details for.|

> Example responses

> Detailed information about the specified movie, including image URL, title, year, average rating, genres, tags, individual ratings, actors, and directors.

```json
{
  "actors": [
    "Leonardo DiCaprio",
    "Joseph Gordon-Levitt"
  ],
  "directors": [
    "Christopher Nolan"
  ],
  "genres": [
    "Action",
    "Adventure",
    "Sci-Fi"
  ],
  "imageUrl": "http://example.com/image.jpg",
  "rating": 8.8,
  "ratingsList": [
    9,
    8,
    10,
    7
  ],
  "tags": [
    "mind-bending",
    "dream",
    "subconscious"
  ],
  "title": "Inception",
  "year": 2010
}
```

<h3 id="get__movies_get-by-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Detailed information about the specified movie, including image URL, title, year, average rating, genres, tags, individual ratings, actors, and directors.|None|

<h3 id="get__movies_get-by-id-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-search">Search</h1>

## post__movies_get-search-results

> Code samples

```shell
# You can also use wget
curl -X POST /movies/get-search-results \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /movies/get-search-results HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "date": [
    0
  ],
  "genres": [
    "string"
  ],
  "numLoaded": 0,
  "ratings": [
    0
  ],
  "searchText": "string",
  "tags": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/movies/get-search-results',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/movies/get-search-results',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/movies/get-search-results', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/movies/get-search-results', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/movies/get-search-results");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/movies/get-search-results", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /movies/get-search-results`

Performs a search query on movies database based on various filters like text, ratings, tags, genres, and date range. Returns a list of movies that match the criteria.

> Body parameter

```json
{
  "date": [
    0
  ],
  "genres": [
    "string"
  ],
  "numLoaded": 0,
  "ratings": [
    0
  ],
  "searchText": "string",
  "tags": [
    "string"
  ]
}
```

<h3 id="post__movies_get-search-results-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|Parameters for the search query.|
|» date|body|[integer]|false|Array containing start and end years to filter movies by their release date.|
|» genres|body|[string]|false|List of genres to filter movies by.|
|» numLoaded|body|integer|false|Number of movies already loaded, used for pagination.|
|» ratings|body|[integer]|false|Array containing minimum and maximum ratings to filter by.|
|» searchText|body|string|false|Text to search for in movie titles, actor names, and director names.|
|» tags|body|[string]|false|List of tags to filter movies by.|

> Example responses

> A list of movies that match the search criteria, along with a flag indicating if all movies have been loaded.

```json
{
  "all_loaded": false,
  "results": [
    {
      "imageUrl": "http://example.com/image.jpg",
      "movieId": 1,
      "rating": 8.8,
      "title": "Inception",
      "year": 2010
    },
    {
      "imageUrl": "http://anotherexample.com/image.jpg",
      "movieId": 2,
      "rating": 9,
      "title": "The Matrix",
      "year": 1999
    }
  ]
}
```

<h3 id="post__movies_get-search-results-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of movies that match the search criteria, along with a flag indicating if all movies have been loaded.|None|

<h3 id="post__movies_get-search-results-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-user-preferences">User Preferences</h1>

## post__movies_user-preferences

> Code samples

```shell
# You can also use wget
curl -X POST /movies/user-preferences \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /movies/user-preferences HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "opinion": 1
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/movies/user-preferences',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/movies/user-preferences',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/movies/user-preferences', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/movies/user-preferences', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/movies/user-preferences");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/movies/user-preferences", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /movies/user-preferences`

Retrieves movies based on user preference indicated by the opinion value. Opinion values correspond to different rating preferences.

> Body parameter

```json
{
  "opinion": 1
}
```

<h3 id="post__movies_user-preferences-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|JSON payload containing the user opinion on movie ratings.|
|» opinion|body|integer|true|User opinion indicating preference. 1 for high-rated (4 to 5), 2 for low-rated (0 to 2), any other value for mid-range rated (2 to 4) movies.|

> Example responses

> A list of movies filtered by user preference based on the opinion provided.

```json
[
  {
    "movieId": 1,
    "rating": 4.5,
    "title": "Highly Rated Movie"
  },
  {
    "movieId": 2,
    "rating": 4.7,
    "title": "Another Highly Rated Movie"
  }
]
```

<h3 id="post__movies_user-preferences-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of movies filtered by user preference based on the opinion provided.|None|

<h3 id="post__movies_user-preferences-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-personality-analysis">Personality Analysis</h1>

## get__personality-skew

> Code samples

```shell
# You can also use wget
curl -X GET /personality-skew \
  -H 'Accept: application/json'

```

```http
GET /personality-skew HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/personality-skew',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/personality-skew',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/personality-skew', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/personality-skew', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/personality-skew");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/personality-skew", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /personality-skew`

Calculate personality skew based on movie preferences.

> Example responses

> A list of personality types with their corresponding movie genres and Pearson coefficients.

```json
{
  "agreeableness": {
    "x": [
      "Family",
      "Adventure"
    ],
    "y": [
      0.9,
      0.88
    ]
  },
  "openness": {
    "x": [
      "Drama",
      "Comedy"
    ],
    "y": [
      0.95,
      0.85
    ]
  }
}
```

<h3 id="get__personality-skew-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of personality types with their corresponding movie genres and Pearson coefficients.|None|

<h3 id="get__personality-skew-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="a-swagger-api-prediction">Prediction</h1>

## post__ratings_prediction

> Code samples

```shell
# You can also use wget
curl -X POST /ratings/prediction \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /ratings/prediction HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "movie": "Inception",
  "users": [
    1,
    2,
    3
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/ratings/prediction',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/ratings/prediction',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/ratings/prediction', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/ratings/prediction', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/ratings/prediction");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/ratings/prediction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /ratings/prediction`

Generates a prediction for a movie rating based on user, genre, and tag biases.

> Body parameter

```json
{
  "movie": "Inception",
  "users": [
    1,
    2,
    3
  ]
}
```

<h3 id="post__ratings_prediction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|JSON payload containing the movie title and a list of user IDs.|
|» movie|body|string|false|Movie title for which the prediction is requested.|
|» users|body|[integer]|false|List of user IDs for bias calculation.|

> Example responses

> The predicted rating for the movie based on biases.

```json
{
  "averageBias": 0.02,
  "averageRating": 4.5,
  "genreBias": -0.05,
  "predictedRating": 4.25,
  "subsetRating": 4.2,
  "tagBias": 0.02,
  "userBias": 0.1
}
```

<h3 id="post__ratings_prediction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The predicted rating for the movie based on biases.|None|

<h3 id="post__ratings_prediction-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## post__users_for-prediction

> Code samples

```shell
# You can also use wget
curl -X POST /users/for-prediction \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /users/for-prediction HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "movie": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/users/for-prediction',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/users/for-prediction',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/users/for-prediction', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/users/for-prediction', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/users/for-prediction");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/users/for-prediction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /users/for-prediction`

Retrieves a list of user IDs for users who have rated a specific movie, limited to the top 5 users.

> Body parameter

```json
{
  "movie": "string"
}
```

<h3 id="post__users_for-prediction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|Parameters for the search query.|
|» movie|body|string|false|The title of the movie to query user ratings for.|

> Example responses

> A list of user IDs who have rated the specified movie

```json
{
  "user_ids": [
    1,
    2,
    3,
    4,
    5
  ]
}
```

<h3 id="post__users_for-prediction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of user IDs who have rated the specified movie|None|

<h3 id="post__users_for-prediction-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>


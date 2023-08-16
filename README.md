# How to get the token for kibana ?
 *  run : 
 ```
  elasticsearch-service-tokens create elastic/kibana my-token01
  ```

#  Basic elasticsearch node/cluster commands
 ## Get info about cluster health
   ```
   GET _cluster/health
   ```
 ## Get info about nodes in a cluster
   ```
   GET _nodes/stats
   ```

# Basic CRUD Operation 
 
## Create an index
    
   ```
    PUT Name-of-the-Index
    
```
## _create Endpoint with id 
 ```
 PUT Name-of-the-Index/_create/id-you-want-to-assign-to-this-document
{
  "field": "value"
}
 ```
## READ
```
GET Name-of-the-Index/_doc/id-of-the-document-you-want-to-retrieve
```
### UPDATE
```
POST Name-of-the-Index/_update/id-of-the-document-you-want-to-update
{
  "doc": {
    "field1": "value",
    "field2": "value",
  }
} 
```
### Delete 
```
DELETE Name-of-the-Index/_doc/id-of-the-document-you-want-to-delete
```

*****************************************************************************

## Retrieve information about documents in an index
```
GET enter_name_of_the_index_here/_search
```
### Get the exact total number of hits
```
GET enter_name_of_the_index_here/_search
{
  "track_total_hits": true
}
```

### Search for data within a specific time range
```
GET enter_name_of_the_index_here/_search
{
  "query": {
    "Specify the type of query here": {
      "Enter name of the field here": {
        "gte": "Enter lowest value of the range here",
        "lte": "Enter highest value of the range here"
      }
    }
  }
}
```
* example 
 ```
 GET news_headlines/_search
{
  "query": {
    "range": {
      "date": {
        "gte": "2015-06-20",
        "lte": "2015-09-22"
      }
    }
  }
}
 ```

### Aggregations
An aggregation summarizes your data as metrics, statistics, and other analytics.
```
GET enter_name_of_the_index_here/_search
{
  "aggs": {
    "name your aggregation here": {
      "specify aggregation type here": {
        "field": "name the field you want to aggregate here",
        "size": state how many buckets you want returned here
      }
    }
  }
}
```
* example :
 ```
 GET news_headlines/_search
{
  "aggs": {
    "by_category": {
      "terms": {
        "field": "category",
        "size": 100
      }
    }
  }
}
 ```

# A combination of query and aggregation request
Search for the most significant term in a category
```
GET enter_name_of_the_index_here/_search
{
  "query": {
    "match": {
      "Enter the name of the field": "Enter the value you are looking for"
    }
  },
  "aggregations": {
    "Name your aggregation here": {
      "significant_text": {
        "field": "Enter the name of the field you are searching for"
      }
    }
  }
}
```
* example :

```
GET news_headlines/_search
{
  "query": {
    "match": {
      "category": "ENTERTAINMENT"
    }
  },
  "aggregations": {
    "popular_in_entertainment": {
      "significant_text": {
        "field": "headline"
      }
    }
  }
}
```
### Precision and Recall
```
GET enter_name_of_index_here/_search
{
  "query": {
    "match": {
      "Specify the field you want to search": {
        "query": "Enter search terms"
      }
    }
  }
}
```
* example :
```
GET news_headlines/_search
{
  "query": {
    "match": {
      "headline": {
        "query": "something here"
      }
    }
  }
}
```
### Increasing Precision
```
GET enter_name_of_index_here/_search
{
  "query": {
    "match": {
      "Specify the field you want to search": {
        "query": "Enter search terms",
        "operator": "and"
      }
    }
  }
}
```
* example :
 ```
 GET news_headlines/_search
{
  "query": {
    "match": {
      "headline": {
        "query": "something something",
        "operator": "and"
      }
    }
  }
}
 ```

### minimum_should_match

This parameter allows you to specify the minimum number of terms a document should have to be included in the search results.

This parameter gives you more control over fine tuning precision and recall of your search.

```
GET enter_name_of_index_here/_search
{
  "query": {
    "match": {
      "headline": {
        "query": "Enter search term here",
        "minimum_should_match": Enter a number here
      }
    }
  }
}
```
* example :
```
GET news_headlines/_search
{
  "query": {
    "match": {
      "headline": {
        "query": "some title something ",
        "minimum_should_match": 3
      }
    }
  }
}
```
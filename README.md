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

# Full text queries

### Searching for phrases using the match_phrase query
If the order and the proximity in which the search terms are found(i.e. phrases) are important in determining the relevance of your search, you use the match_phrase query.
```
GET Enter_name_of_index_here/_search
{
  "query": {
    "match_phrase": {
      "Specify the field you want to search": {
        "query": "Enter search terms"
      }
    }
  }
}
```
example :
```
GET news_headlines/_search
{
  "query": {
    "match_phrase": {
      "headline": {
        "query": "Shape of You"
      }
    }
  }
}
```
### Running a match query against multiple fields
The multi_match query runs a match query on multiple fields and calculates a score for each field. Then, it assigns the highest score among the fields to the document.

This score will determine the ranking of the document within the search results.

syntax 
```
GET Enter_the_name_of_the_index_here/_search
{
  "query": {
    "multi_match": {
      "query": "Enter search terms here",
      "fields": [
        "List the field you want to search over",
        "List the field you want to search over",
        "List the field you want to search over"
      ]
    }
  }
}
```
example 

```
GET news_headlines/_search
{
  "query": {
    "multi_match": {
      "query": "Michelle Obama",
      "fields": [
        "headline",
        "short_description",
        "authors"
      ]
    }
  }
}
```
### Per-field boosting
To improve the precision of your search, you can designate one field to carry more weight than the others.

This can be done by boosting the score of the field headline(per-field boosting). This is notated by adding a carat(^) symbol and number 2 to the desired field as shown below.

syntax 

```
GET Enter_the_name_of_the_index_here/_search
{
  "query": {
    "multi_match": {
      "query": "Enter search terms",
      "fields": [
        "List field you want to boost^2",
        "List field you want to search over",
        "List field you want to search over"
      ]
    }
  }
}
```
example 

```
GET news_headlines/_search
{
  "query": {
    "multi_match": {
      "query": "Michelle Obama",
      "fields": [
        "headline^2",
        "short_description",
        "authors"
      ]
    }
  }
}
```

### multi_match query to search for a phrase

example :

```
GET news_headlines/_search
{
  "query": {
    "multi_match": {
      "query": "party planning",
      "fields": [
        "headline^2",
        "short_description"
      ]
    }
  }
}
```

### Improving precision with phrase type match

You can improve the precision of a multi_match query by adding the "type":"phrase" to the query.

The phrase type performs a match_phrase query on each field and calculates a score for each field. Then, it assigns the highest score among the fields to the document.

syntax 

```
GET Enter_the_name_of_the_index_here/_search
{
  "query": {
    "multi_match": {
      "query": "Enter search phrase",
      "fields": [
        "List field you want to boost^2",
        "List field you want to search over",
        "List field you want to search over"
      ],
      "type": "phrase"
    }
  }
}
```

example :

```
GET news_headlines/_search
{
  "query": {
    "multi_match": {
      "query": "party planning",
      "fields": [
        "headline^2",
        "short_description"
      ],
      "type": "phrase"
    }
  }
}
```

# Combined Queries

### Bool Query

The bool query retrieves documents matching boolean combinations of other queries.

With the bool query, you can combine multiple queries into one request and further specify boolean clauses to narrow down your search results.

There are four clauses to choose from:

    must
    must_not
    should
    filter

You can build combinations of one or more of these clauses. Each clause can contain one or multiple queries that specify the criteria of each clause.

These clauses are optional and can be mixed and matched to cater to your use case. The order in which they appear does not matter either!

Syntax:

```
GET name_of_index/_search
{
  "query": {
    "bool": {
      "must": [
        {One or more queries can be specified here. A document MUST match all of these queries to be considered as a hit.}
      ],
      "must_not": [
        {A document must NOT match any of the queries specified here. It it does, it is excluded from the search results.}
      ],
      "should": [
        {A document does not have to match any queries specified here. However, it if it does match, this document is given a higher score.}
      ],
      "filter": [
        {These filters(queries) place documents in either yes or no category. Ones that fall into the yes category are included in the hits. }
      ]
    }
  }
}

```

* The must clause
 example 

 ```
 GET news_headlines/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match_phrase": {
          "headline": "Michelle Obama"
         }
        },
        {
          "match": {
            "category": "POLITICS"
          }
        }
      ]
    }
  }
}
 ```

* The must_not clause

```
GET news_headlines/_search
{
  "query": {
    "bool": {
      "must": {
        "match_phrase": {
          "headline": "Michelle Obama"
         }
        },
       "must_not":[
         {
          "match": {
            "category": "WEDDINGS"
          }
        }
      ]
    }
  }
}
```

* The should clause

```
GET news_headlines/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match_phrase": {
          "headline": "Michelle Obama"
          }
         }
        ],
       "should":[
         {
          "match_phrase": {
            "category": "BLACK VOICES"
          }
        }
      ]
    }
  }
}
```
# The filter clause

The filter clause contains filter queries that place documents into either "yes" or "no" category.

he filter clause only includes documents that fall into the yes category.

Syntax:
```
GET Enter_name_of_the_index_here/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "Enter match or match_phrase here": {
          "Enter the name of the field": "Enter the value you are looking for" 
         }
        }
        ],
       "filter":{
          "range":{
             "date": {
               "gte": "Enter lowest value of the range here",
               "lte": "Enter highest value of the range here"
          }
        }
      }
    }
  }
}

```
example 

```
GET news_headlines/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match_phrase": {
          "headline": "Michelle Obama"
          }
         }
        ],
       "filter":{
          "range":{
             "date": {
               "gte": "2014-03-25",
               "lte": "2016-03-25"
          }
        }
      }
    }
  }
}
```

# Adding multiple queries under the should clause

This approach ensures that you maintain a high recall but also offers a way to present more precise search results at the top of your search results.

Syntax:

```
GET Enter_name_of_the_index_here/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "Enter match or match_phrase here": {
            "Enter the name of the field": "Enter the value you are looking for"
          }
        }
      ],
      "should": [
        {
          "Enter match or match_phrase here": {
            "Enter the name of the field": "Enter the value you are looking for"
          }
        },
        {
          "Enter match or match_phrase here": {
            "Enter the name of the field": "Enter the value you are looking for"
          }
        },
        {
          "Enter match or match_phrase here": {
            "Enter the name of the field": "Enter the value you are looking for"
          }
        }
      ]
    }
  }
}

```

example :

```
GET news_headlines/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "headline": "Michelle Obama"
          }
        }
      ],
      "should": [
        {
          "match": {
            "headline": "Becoming"
          }
        },
        {
          "match": {
            "headline": "women"
          }
        },
        {
          "match": {
            "headline": "empower"
          }
        }
      ]
    }
  }
}
```



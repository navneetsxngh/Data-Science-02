## HTTP Status Codes

### 1xx – Informational
```
| Code | Name                | Meaning                                 |
| ---- | ------------------- | --------------------------------------- |
| 100  | Continue            | Request received, continue sending body |
| 101  | Switching Protocols | Server switching protocols              |
| 102  | Processing          | Request received but not completed yet  |

```

### 2xx – Success
```
| Code | Name       | Meaning                            | When to Use         |
| ---- | ---------- | ---------------------------------- | ------------------- |
| 200  | OK         | Request successful                 | GET request success |
| 201  | Created    | Resource created                   | POST success        |
| 202  | Accepted   | Request accepted, processing later | Async tasks         |
| 204  | No Content | Success but no response body       | DELETE success      |

```

### 3xx – Redirection
```
| Code | Name              | Meaning                    |
| ---- | ----------------- | -------------------------- |
| 301  | Moved Permanently | Resource permanently moved |
| 302  | Found             | Temporary redirect         |
| 304  | Not Modified      | Cached version can be used |

```

### 4xx – Client Errors
```
| Code | Name                 | Meaning                 | When to Use          |
| ---- | -------------------- | ----------------------- | -------------------- |
| 400  | Bad Request          | Invalid request format  | Validation errors    |
| 401  | Unauthorized         | Authentication required | No login token       |
| 403  | Forbidden            | Access denied           | No permission        |
| 404  | Not Found            | Resource not found      | Patient ID not found |
| 405  | Method Not Allowed   | Wrong HTTP method       | POST on GET route    |
| 409  | Conflict             | Data conflict           | Duplicate entry      |
| 422  | Unprocessable Entity | Validation failed       | FastAPI validation   |
```

### 5xx – Server Errors
```
| Code | Name                  | Meaning                   |
| ---- | --------------------- | ------------------------- |
| 500  | Internal Server Error | Unexpected server crash   |
| 502  | Bad Gateway           | Invalid upstream response |
| 503  | Service Unavailable   | Server down or overloaded |
| 504  | Gateway Timeout       | Upstream timeout          |

```
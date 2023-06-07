# Gym-tools-endpoint

| Information  | Value                                  |
|--------------|----------------------------------------|
| Docker Image | - |
|   Port Open  |                  8001                  |


| Endpoint | Method |             Content Type            |                 Description                |
|:--------:|:------:|:-----------------------------------:|:------------------------------------------:|
|     /    |   GET  |                 None                |              This is spofity!              |
|     /    |  POST  |         multipart/form-data         |        Makes prediction from our model     |

Checkout all our pre-trained model through this [link]([https://drive.google.com/drive/folders/1A7N_McAxnxrThlDyArJXr0_k-nHPDfiI](https://drive.google.com/drive/folders/1UwIH6epKdSkBNr84h3S6yltNk1BjCSKD?usp=sharing)).  

## Example Usage 

### Endpoint `/`

- **Method**: GET
- **Content Type**: application/json

**Description**: This endpoint provides information about Spofity.

Example Request:

```
GET http://localhost:8001/
```

Example Response:

```
Status: 200 OK
Content-Type: application/json
```
```JSON
{
    "This is spofity!"
}
```

### Endpoint `/`

- **Method**: POST
- **Content Type**: multipart/form-data

**Description**: This endpoint is used to make predictions using the deployed model.

Example Request:
```
POST http://localhost:8001/
Content-Type: multipart/form-data
```

```JSON
{
  "file": image_data
}
```

Example Response:

```
Status: 200 OK
Content-Type: application/json
```
```JSON
{
  "id": "3",
  "name": "Gym ball",
  "accuracy": 0.999998927116394,
  "time_predict": 0.09
}

```

C23-PC637 ML Teams.

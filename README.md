# Nigeria States & LGA API 🌍

A lightweight REST API providing all Nigerian states, Local Government Areas (LGAs), and country/state relationships in JSON format. Perfect for address forms, location-based apps, and data validation.

## 🔑 Features

* Get all **countries** (with Nigeria as default focus).

* Fetch all **36 Nigerian states** + FCT.

* Retrieve **LGAs by state** (e.g., Lagos, Kano, Rivers).

* Fast, scalable, and developer-friendly JSON responses.

## 📚 API Endpoints

### **Location Data**

| Endpoint | Method | Description |
| ----- | ----- | ----- |
| `/api/v1/location/countries` | `GET` | Get all supported countries |
| `/api/v1/location/states` | `GET` | Get all states in Nigeria |
| `/api/v1/location/states/{country_id}` | `GET` | Get states by country ID |
| `/api/v1/location/lgas` | `GET` | Get all LGAs in Nigeria |
| `/api/v1/location/lgas/{state_id}` | `GET` | Get LGAs by state ID |

## 🚀 Usage Examples

### 1. Get all countries

```
GET /api/v1/location/countries

```

**Response:**

```
{
  "data": [
    { "id": 1, "name": "Nigeria", "code": "NG" },
    { "id": 2, "name": "Ghana", "code": "GH" }
  ]
}

```

### 2. Get all Nigerian states

```
GET /api/v1/location/states

```

**Response:**

```
{
  "data": [
    { "id": 1, "name": "Lagos", "country_id": 1 },
    { "id": 2, "name": "Kano", "country_id": 1 }
  ]
}

```

### 3. Get LGAs by state ID (e.g., Lagos)

```
GET /api/v1/location/lgas/1

```

**Response:**

```
{
  "data": [
    { "id": 1, "name": "Agege", "state_id": 1 },
    { "id": 2, "name": "Alimosho", "state_id": 1 }
  ]
}

```

## 🛠 Setup (Local Development)

1. **Clone the repo:**

   ```
   git clone [https://github.com/zenoftech/nigeria-states-lga-api.git](https://github.com/zenoftech/nigeria-states-lga-api.git)
   cd nigeria-states-lga-api

   ```

2. **Create and activate a virtual environment:**

   ```
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

   ```

3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   # (Ensure requirements.txt contains: fastapi, uvicorn, sqlalchemy, psycopg2-binary, pydantic)

   ```

6. **Run the server:**

   ```
   uvicorn app.main:app --reload

   ```

   (Adjust `app.main:app` if your main FastAPI app is in a different module, e.g., `main:app` if `main.py` is in the root and `app` is the FastAPI instance name)

   API will be live at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## 🌐 Live Demo
<!-- 
Try the API live: `https://api.example.com/v1/location/states` (Replace `api.example.com` with your actual deployed URL on Railway). -->

## 🤝 Contributing

Contributions are welcome! Open an issue or submit a PR for:

* Additional countries/states.
* Performance improvements.

## 📜 License

MIT © Muktar Aliyu 

# Dapr-Demo

## [安裝 Dapr](https://docs.dapr.io/getting-started/install-dapr-cli/)

## 啟動API

```
# 開新終端機
cd py-app/
dapr run --app-id app-1 --app-port 3002 --dapr-http-port 3500 -- python3 app.py
```

## 啟動UI

```
# 開新終端機
cd ui/
streamlit run app.py
```

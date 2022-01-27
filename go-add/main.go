package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
)

func main() {
	type ADD struct {
		A, B float64
	}

	http.HandleFunc("/sum", func(rw http.ResponseWriter, r *http.Request) {
		log.Println("from --> ", r.RemoteAddr)
		var req = requestJSON[ADD](r)
		resJSON(rw, req.A+req.B)
	})

	count := 0
	http.HandleFunc("/count", func(rw http.ResponseWriter, r *http.Request) {
		log.Println("from --> ", r.RemoteAddr)
		count++
		resJSON(rw, count)
	})

	http.HandleFunc("/upload", func(rw http.ResponseWriter, r *http.Request) {
		log.Println("from --> ", r.RemoteAddr)
		d := requestBytes(r)
		resRaw(rw, d)
	})

	log.Println("Serving ...")
	http.ListenAndServe(":3001", nil)
}

func requestJSON[T any](r *http.Request) T {
	var req T
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		panic(err)
	}

	return req
}

func requestBytes(r *http.Request) []byte {
	b, err := io.ReadAll(r.Body)
	if err != nil {
		panic(err)
	}

	return b
}

func resJSON(rw http.ResponseWriter, data any) {
	err := json.NewEncoder(rw).Encode(data)
	if err != nil {
		panic(err)
	}
}
func resRaw(rw http.ResponseWriter, data []byte) {
	_, err := rw.Write(data)
	if err != nil {
		panic(err)
	}
}

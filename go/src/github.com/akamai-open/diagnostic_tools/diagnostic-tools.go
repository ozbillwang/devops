package main

import (
	"fmt"
	"github.com/akamai-open/AkamaiOPEN-edgegrid-golang"
	"io/ioutil"
	"net/http"
)

func main() {
	client := http.Client{}

	config := edgegrid.InitConfig("~/.edgerc", "default")

	req, _ := http.NewRequest("GET", fmt.Sprintf("https://%sdiagnostic-tools/v1/locations", config.Host), nil)
	req = edgegrid.AddRequestHeader(config, req)
	resp, _ := client.Do(req)
	byt, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(byt))


	req, _ = http.NewRequest("GET", fmt.Sprintf("https://%sdiagnostic-tools/v1/dig", config.Host), nil)
	q := req.URL.Query()
	q.Add("hostname", "developer.akamai.com")
	q.Add("queryType", "A")
	q.Add("location", "Auckland, New Zealand")
	req.URL.RawQuery = q.Encode()
	req = edgegrid.AddRequestHeader(config, req)
	resp, _ = client.Do(req)
	byt, _ = ioutil.ReadAll(resp.Body)
	fmt.Println(string(byt))
}

import http from "k6/http";
import { check, sleep } from "k6";

export let options = {
    vus: 100,          
    duration: "2s", 
};

export default function () {
    let res = http.get("http://127.0.0.1:5000/posts");
    check(res, {
        "status is 200": (r) => r.status === 200,
        "body not empty": (r) => r.body.length > 0
    });
    sleep(1);
}

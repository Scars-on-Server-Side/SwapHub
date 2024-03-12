import * as React from "react";
import Router from "./Router";

import axios from "axios";
import { useState, useEffect } from "react";


function Auth(props) {
    const [accessToken, setAccessToken] = useState<string>("");
    const [refreshToken, setRefreshToken] = useState<string>("");
    const [username, setUsername] = useState<string>("admin");
    const [password, setPassword] = useState<string>("admin");

    const fetchLogin = async (username: string, password: string) => {
        await axios
            .post(
                "http://localhost:80/api/v1/token/",
                {
                    username: username,
                    password: password
                },
                {
                    headers: {
                        "Content-Type": "application/json",
                    }
                }
            )
            .then((response) => {
                setAccessToken(response.data.access);
                setRefreshToken(response.data.refresh);
            })
            /* Ошибка Auth.tsx + StartPage.tsx
            {
              "detail": "Authorization header must contain two space-delimited values",
              "code": "bad_authorization_header"
            }
            Мы получаем токен в ответе, но он или не успевает сохраниться или не передаеться. */
            .catch((error) => {
                console.error(error);
            });
    }

    useEffect(() => {
        fetchLogin(username, password);
        //fetchLogin("admin", "admin");
    });

    return (
        <Router accessToken={accessToken} />
    )
}

export default Auth;

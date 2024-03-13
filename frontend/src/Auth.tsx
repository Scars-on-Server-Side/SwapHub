import * as React from "react";
import Router from "./Router";

import axios from "axios";
import { useState, useEffect } from "react";


function Auth() {
    const [accessToken, setAccessToken] = useState<string>(localStorage.getItem('accessToken') || '');
    const [refreshToken, setRefreshToken] = useState<string>(localStorage.getItem('accessToken') || '');
    const [username, setUsername] = useState<string>("admin");
    const [password, setPassword] = useState<string>("admin");

    const login = async (username: string, password: string) => {
        await axios
            .post("http://localhost:80/api/v1/token/",{username: username, password: password})
            .then((response) => {
                const { access, refresh } = response.data;
                setAccessToken(access);
                setRefreshToken(refresh);
                localStorage.setItem('accessToken', access);
                localStorage.setItem('refreshToken', refresh);
            })
            .catch((error) => {
                console.error(error);
            });
    }

    const refresh = async () => {
        await axios
            .post('http://localhost:80/api/v1/token/refresh/', { refresh: refreshToken })
            .then((response) => {
                const { access } = response.data;
                setAccessToken(access);
                localStorage.setItem('accessToken', access);
            })
            .catch((error) => {
                console.error(error);
                if (error.response.status === 400) { 
                    login(username, password)
                }
            })
    };

    const logout = () => {
        setAccessToken('');
        setRefreshToken('');
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
    };

    

    const handleUnauthorized = () => { refresh(); }
    const handleLogout = () => { logout(); }

    return (
        <Router
            accessToken={accessToken}
            onUnauthorized={handleUnauthorized}
            onLogout={handleLogout}
        />
    )
}

export default Auth;

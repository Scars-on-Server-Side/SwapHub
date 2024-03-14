import * as React from "react";
import Router from "./Router";

import axios from "axios";
import { useState, useEffect } from "react";


function Auth() {
    const [accessToken, setAccessToken] = useState<string>(localStorage.getItem('accessToken') || '');
    const [refreshToken, setRefreshToken] = useState<string>(localStorage.getItem('accessToken') || '');

    const login = async (username: string, password: string) => {
        await axios
            .post("http://localhost:80/api/v1/token/",{username: username, password: password})
            .then((response) => {
                const { access, refresh } = response.data;
                setAccessToken(access);
                setRefreshToken(refresh);
                localStorage.setItem('accessToken', access);
                localStorage.setItem('refreshToken', refresh);
                alert("You logged in successfully!!!");
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
                    alert("Register first before login!!!")
                }
            })
    };

    const logout = () => {
        setAccessToken('');
        setRefreshToken('');
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
    };

    const handleLogin = (formData) => { login(formData.username, formData.password); }    
    const handleUnauthorized = () => { refresh(); }
    const handleLogout = () => { logout(); }

    return (
        <Router
            accessToken={accessToken}
            onUnauthorized={handleUnauthorized}
            onLogout={handleLogout}
            onLogin={handleLogin}
        />
    )
}

export default Auth;

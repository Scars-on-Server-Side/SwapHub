import React from "react";
import Header from "./components/header/Header.tsx";
import AuthForm from "./components/auth/AuthForm.tsx";


function AuthFormPage(props) {

    const handleClickAvatar = () => {
        alert("Avatar clicked");
    }
    const handleLogin = (formData) => {props.onLogin(formData);}

    return (
        <div className="AuthFormPage">
            <Header onClickAvatar={handleClickAvatar} />
            <AuthForm onLogin={handleLogin} />
        </div>
    )
}

export default AuthFormPage;

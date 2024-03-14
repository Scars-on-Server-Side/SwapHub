import React, { useState } from "react";


function AuthForm(props) {
    const [inputUsername, setInputUsername] = useState('');
    const [inputPassword, setInputPassword] = useState('');

    const changeUsernameHandler = (event) => {
        setInputUsername(event.target.value);
    }
    const changePasswordHandler = (event) => {
        setInputPassword(event.target.value);
    }


    const submitHandler = (event) => { 
        event.preventDefault();

        const formData = {
            username: inputUsername,
            password: inputPassword
        };
        props.onLogin(formData);
        
        setInputUsername('');
        setInputPassword('');
    };

    return (
        <form action="AuthForm" onSubmit={submitHandler}>
            <div className="AuthForm-username">
                <label htmlFor='useraname'>Username</label>
                <input id='username' type="text" value={inputUsername} onChange={changeUsernameHandler} />
            </div>
            <div className="AuthForm-password">
                <label htmlFor='password'>Password</label>
                <input id='password' type="text" value={inputPassword} onChange={changePasswordHandler} />
            </div>
            <div className='AuthForm-actions'>
                <button type='submit'>Login</button>
            </div>
        </form>
    )
}

export default AuthForm;

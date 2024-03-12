import React from "react";
import "./StartPage.css";
import Header from "./components/header/Header.tsx";
import Start from "./components/start/Start.tsx";

import axios from "axios";
import { useState, useEffect } from "react";

function StartPage(props) {
  // Define state variables for startThings and things
  const [startThings, setStartThings] = useState([{}]);
  const accessToken = props.accessToken;
  const host = "http://localhost";

  // Function to fetch things data from the API
  const fetchStartThings = async () => {
    await axios
      .get("http://localhost:80/api/v1/thing/start/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
          /* Ошибка Auth.tsx + StartPage.tsx
            {
              "detail": "Authorization header must contain two space-delimited values",
              "code": "bad_authorization_header"
            }
            Мы получаем токен в ответе, но он или не успевает сохраниться или не передаеться. */

        },
      })
      .then((response) => {
        setStartThings(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  // Fetch things when component mounts
  useEffect(() => {
    fetchStartThings();
  });

  // Function to handle avatar click
  const handleClickAvatar = () => {
    alert("Avatar clicked");
    console.log(startThings);
  };

  // Render Header and Start components with props
  return (
    <div className="StartPage">
      <Header onClickAvatar={handleClickAvatar} />
      <Start startThings={startThings} host={host} />
    </div>
  );
}

export default StartPage;

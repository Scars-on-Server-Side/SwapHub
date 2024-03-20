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

  // Function to fetch things data from the API
  const fetchStartThings = async () => {
    await axios
      .get("http://localhost:80/api/v1/thing/start/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
        },
      })
      .then((response) => {
        setStartThings(response.data);
      })
      .catch((error) => {
        console.error(error);
        if (error.response.status === 401) { 
          props.onUnauthorized()
        }
      });
  };

  // Fetch things when component mounts
  useEffect(() => {
    fetchStartThings();
  }, [accessToken]);

  // Function to handle avatar click
  const handleClickAvatar = () => {
    props.onLogout();
  };

  // Render Header and Start components with props
  return (
    <div className="StartPage">
      <Header onClickAvatar={handleClickAvatar} />
      <Start startThings={startThings} />
    </div>
  );
}

export default StartPage;

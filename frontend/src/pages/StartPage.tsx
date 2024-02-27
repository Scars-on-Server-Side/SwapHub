import React from "react";
import "./StartPage.css";
import Header from "./components/header/Header.tsx";
import Start from "./components/start/Start.tsx";

import axios from "axios";
import { useState, useEffect } from "react";

function StartPage() {
  // Define state variables for startThings and things
  const [startThings, setStartThings] = useState([{}]);

  // Function to fetch things data from the API
  const fetchStartThings = async () => {
    await axios
      .get("http://localhost:80/api/v1/thing/start/", {
        headers: {
          "Content-Type": "application/json",
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
  }, []);

  // Function to handle avatar click
  const handleClickAvatar = () => {
    alert("Avatar clicked");
    console.log(startThings);
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
